from bs4 import BeautifulSoup as bs, Comment, NavigableString
import requests
from main.logger.logger import Logger


class TagExplorer(object):
    """html tag explorer class"""
    """BeautifulSoup based"""

    HTML_PARSER = 'lxml'

    def __init__(self, url=None, filter_list=None):
        self.log = Logger(self.__class__.__name__).log

        if filter_list is None:
            filter_list = []

        self.url = url

        self.__root__ = None
        self.__stack__ = None
        if self.url is not None:
            self.set_url(url)

        self.filter_list = filter_list

    def __repr__(self):
        return "%s url:%s" % (self.__class__.__name__, self.url)

    def __len__(self):
        return len(self.__stack__)

    def __children(self):
        """
        return current children

        :return BeautifulSoup object
        """
        return self.__stack__[-1].contents

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

    def set_url(self, url):
        """set TXP instance's target url

        :param
        url : str

        :return None
        """
        html = " ".join(requests.get(url).text.split())
        self.__root__ = bs(html, self.HTML_PARSER)
        self.__stack__ = [self.__root__]

    def set_filter(self, *args):
        """set TXP instance's filter

        :param
        args : iterable

        :return None
        """
        self.filter_list = args

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
        return str(self.__filter_soup(self.__stack__[-1]))

    def move_down(self, idx):
        """
        move down from current node to idx'th child

        :param
        idx : int

        :return None
        """
        self.log.error('at move_down ' + str(idx) + ' ' + str(type(idx)))
        self.__stack__ += [self.__stack__[-1].contents[idx]]

    def move_up(self):
        """
        move up form current node to parent node

        :return None
        """
        if len(self.__stack__) > 1:
            self.__stack__.pop()

    def trace_stack(self):
        """
        return stack trace

        :return: list
        """
        ret = []
        for idx, item in enumerate(self.__stack__[1:]):
            cur = self.__root__.find(item.name, item.attrs)
            ret += [(idx, cur.name, cur.attrs)]
        return ret
