from bs4 import BeautifulSoup as bs, Comment, NavigableString
import requests
from main.logger.logger import Logger
import json


class TagExplorer(object):
    """
    html tag explorer class
    BeautifulSoup based
    """

    HTML_PARSER = 'lxml'

    def __init__(self, url=None, filter_list=None):
        """
        :param url: str option
        :param filter_list: iterable

        """
        self.log = Logger(self.__class__.__name__).log

        if filter_list is None:
            filter_list = []

        self.__root__ = None
        self.stack_soup = None
        self.stack_idx = None
        self.tag_name = None
        self.attr_key = None
        self.filter_list = filter_list
        self.parse_form = None
        if url is not None:
            self.set_root(url)

    def __len__(self):
        return len(self.stack_soup)

    def __children(self):
        """
        return current children

        :return BeautifulSoup object
        """
        return self.stack_soup[-1].contents

    def __filter_soup(self, soup):
        """
        filter bs.object

        :param soup: beautifulSoup object

        :return: beautifulSoup object
        """
        # todo hack implement deep copy
        # deep copy bs object
        soup = bs(str(soup), self.HTML_PARSER)

        # if self.filter_comment is True:
        #     for item in soup.findAll(text=lambda text: isinstance(text, Comment)):
        #         item.extract()

        for filter_ in self.filter_list:
            for item in soup.findAll(filter_):
                item.extract()

        return soup

    def __filter_tags(self, tags):
        """
        deprecated?

        :param tags:

        :return:
        """
        ret = []
        for idx, name, attrs in tags:
            if name not in self.filter_list:
                ret += [(idx, name, attrs)]
        return ret

    def set_root(self, url):
        """
        :param
        url : str

        :return None
        """
        html = " ".join(requests.get(url).text.split())
        self.__root__ = bs(html, self.HTML_PARSER)
        self.stack_soup = [self.__root__]
        self.stack_idx = [None]
        return True

    def set_filter(self, *args):
        """
        :param
        args : iterable

        :return None
        """
        self.filter_list = args

    def get_filter(self):
        return self.filter_list

    def add_filter(self, name):
        self.filter_list += [name]

    def del_filter(self, name):
        idx = self.filter_list.index(name)
        self.filter_list.pop(idx)
        return True

    def children_tag(self):
        """return current children's tag list

        :return list
        """
        ret = []
        for idx, child in enumerate(self.__children()):
            if type(child) is NavigableString:
                name = "NavigableString"
            elif type(child) is Comment:
                name = 'comment'
            else:
                name = child.name

            if hasattr(child, "attrs"):
                attrs = child.attrs
            else:
                attrs = None

            if name not in self.filter_list:
                ret += [(idx, name, attrs,)]
        return ret

    def current_html(self):
        """
        return current node's html

        :return str
        """
        return str(self.__filter_soup(self.stack_soup[-1]))

    def move_down(self, idx):
        """
        move down from current node to idx'th child

        :param
        idx : int

        """
        # self.log.error('at move_down ' + str(idx) + ' ' + str(type(idx)))
        self.stack_soup += [self.stack_soup[-1].contents[idx]]
        self.stack_idx += [idx]
        return True

    def move_up(self):
        """
        move up form current node to parent node
        """
        if len(self.stack_soup) > 1:
            self.stack_soup.pop()
            self.stack_idx.pop()
        return True

    def trace_stack(self):
        """
        return stack trace

        :return: list
        select idx, tag's name, tag's attrs
        """
        ret = []
        for idx, item in zip(self.stack_idx[1:], self.stack_soup[1:]):
            cur = self.__root__.find(item.name, item.attrs)
            ret += [(idx, cur.name, cur.attrs)]
        return ret

    # todo refactoring and it is pain in my ass
    @staticmethod
    def __extract(tag_name=None, attr_key=None, trace_stack=None, root=None):
        """
        extract all tags like current tag's signature

        search will start from self.__root__
        filter by trace_stack's name and attrs
        item is beautifulsoup object so

        :param tag_name: string
        :param attr_key: string
        :return: list
        """

        q = [root]
        for idx, name, attrs in trace_stack:
            new_q = []

            for item in q:
                for child in item.children:
                    if child.name == name and child.attrs == attrs:
                        new_q += [child]

            q = new_q[:]

        # filter tags
        if tag_name is not None:
            ret = []
            for tags in q:
                for tag in tags.find_all(tag_name):
                    if attr_key in tag.attrs:
                        ret += [tag.attrs[attr_key]]
                    else:
                        ret += [tag]
        else:
            ret = q

        return list(map(str, ret))

    def extract_from_parse_form(self, url, parse_form=None):
        if parse_form is None:
            parse_form = self.parse_form

        tag_name = parse_form['tag_name']
        attr_key = parse_form['attr_key']
        trace_stack = parse_form['stack_trace']
        html = " ".join(requests.get(url).text.split())
        root = bs(html, self.HTML_PARSER)
        return self.__extract(tag_name, attr_key, trace_stack, root)

    def extract_current(self, tag_name=None, attr_key=None):
        self.tag_name = tag_name
        self.attr_key = attr_key

        return self.__extract(tag_name, attr_key, self.trace_stack(), self.__root__)

    def export_parse_form(self):
        """
        """
        ret = {
            "stack_trace": self.trace_stack(),
            "tag_name": self.tag_name,
            "attr_key": self.attr_key,
            "filter_list": self.filter_list,
        }

        return json.dumps(ret)

    def import_parse_form(self, parse_form):
        self.parse_form = json.loads(parse_form)
        return True
