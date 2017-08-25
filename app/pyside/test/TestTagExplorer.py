from main.BaseTest import BaseTest
from main.tagExplorer.TagExplorer import TagExplorer

URL_SITE = """http://bbs.ruliweb.com/best/humor?&page=%d"""

# test resource
TEST_URL = "http://bbs.ruliweb.com/best/humor?&page=1"


class TestTagExplorer(BaseTest):
    txp = None

    @staticmethod
    def set_filter(txp, *args):
        txp.set_filter(*args)
        return txp

    def test_00_init(self):
        self.chaining(None)
        self.txp = TagExplorer()

    def test_01_set_root(self):
        self.chaining(self.test_00_init)
        self.txp.set_root(TEST_URL)

        # todo ....
        assert True

    def test_02_current_html(self):
        self.chaining(self.test_01_set_root)
        ret = self.txp.current_html()
        self.log(ret)
        assert True

    def test_03_children_tag(self):
        self.chaining(self.test_01_set_root)
        ret = self.txp.children_tag()
        self.log(ret)

        assert True

    def test_04_set_filter(self):
        self.chaining(self.test_01_set_root)

        before = self.txp.children_tag()

        self.txp.set_filter('comment')

        after = self.txp.children_tag()

        self.log(before)
        self.log(after)

        assert before != after

    def test_05_move_down(self):
        self.chaining(self.test_04_set_filter())
        before = self.txp.children_tag()

        self.txp.move_down(7)

        after = self.txp.children_tag()

        self.log(before)
        self.log(after)

        assert before != after

    def test_06_move_up(self):
        self.chaining(self.test_04_set_filter)

        self.txp.move_down(7)
        before = self.txp.children_tag()

        self.txp.move_up()

        after = self.txp.children_tag()

        self.log(before)
        self.log(after)

        assert before != after

    def test_07_trace_stack(self):
        self.chaining(self.test_04_set_filter)

        self.txp.set_filter('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                            'noscript', 'comment', 'NavigableString')

        before = self.txp.trace_stack()
        self.txp.children_tag()
        self.txp.move_down(7)
        self.txp.trace_stack()

        after = self.txp.trace_stack()
        self.txp.children_tag()

        self.log(before)
        self.log(after)

        assert before != after

    def test_08_exploring(self):
        self.chaining(self.test_04_set_filter)
        self.txp.set_filter('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                            'noscript', 'comment', 'NavigableString')

        move_down_list = [7, 5, 7, 7, 1, 3, 1, 5, 1, 5, 1, 3]
        for idx in move_down_list:
            trace_stack = self.txp.trace_stack()
            children_tag = self.txp.children_tag()
            self.txp.move_down(idx)
            self.log(trace_stack)
            self.log(children_tag)

        trace_stack = self.txp.trace_stack()
        self.log(trace_stack)
        children_tag = self.txp.children_tag()
        self.log(children_tag)

        ret = self.txp.current_html()
        self.log(ret)

    def test_09_extract_current(self):
        self.chaining(self.test_08_exploring)
        ret = self.txp.extract_current()
        self.log(ret)

        ret = self.txp.extract_current('a', 'href')
        self.log(ret)

    def test_10_export_parse_form(self):
        self.chaining(self.test_09_extract_current)
        ret = self.txp.export_parse_form()
        self.log(ret)

    def test_11_import_parse_form(self):
        self.chaining(self.test_10_export_parse_form)
        parse_form = self.txp.export_parse_form()
        self.log(parse_form)
        parse_form = str(parse_form)

        self.txp.import_parse_form(parse_form)

    def test_12_extract_from_parse_form(self):
        self.chaining(self.test_11_import_parse_form)
        ret = self.txp.extract_from_parse_form(TEST_URL)
        self.log(ret)
        pass

    def test_13_get_filter(self):
        self.chaining(self.test_01_set_root())

        filter_list = ('comment',)
        self.txp.set_filter(*filter_list)

        after = self.txp.get_filter()
        self.log(after)
        self.log(filter_list)
        assert filter_list == after

    def test_14_add_filter(self):
        self.chaining(self.test_01_set_root())

        before = self.txp.get_filter()
        assert before == []

        ret = self.txp.add_filter('comment')

        after = self.txp.get_filter()
        assert after == ['comment']
        self.log(ret)
        self.log(after)

    def test_15_del_filter(self):
        self.chaining(self.test_01_set_root())
        self.txp.add_filter('comment')
        self.txp.add_filter('div')

        before = self.txp.get_filter()
        self.log(before)

        ret = self.txp.del_filter('comment')
        self.log(ret)

        after = self.txp.get_filter()
        self.log(after)

