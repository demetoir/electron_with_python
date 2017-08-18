import zerorpc
import json
from nose import with_setup
from main.util.util import *

URL_SITE = """http://bbs.ruliweb.com/best/humor?&page=1"""
# add PyServer directory to system path
try:
    import os
    import sys

    path = os.path.abspath(__file__)
    path = path.split(os.sep)
    path = path[:path.index("pyside") + 1]
    sys.path.append(os.sep.join(path))

    del os
    del sys
except Exception as e:
    print(e)
    exit(-1)


# TODO add assertion



def connect_zerorpc(cmd, *args, print_=False):
    conn = zerorpc.Client()
    conn.connect("tcp://127.0.0.1:4242")
    method = getattr(conn, cmd)
    ret = method(*args)
    conn.close()

    if print_:
        print('cmd : %s , args : %s ' % (cmd, argsToStr(args)))
        if type(ret) is list:
            for i in ret:
                print(i)
        else:
            print(ret)
        print()

    return ret


def setup_func(*func_list):
    for func in func_list:
        func()
    pass


def teardown_func():
    pass


class TestPyServerConnection:
    @with_setup(setup_func, teardown_func)
    def test_00_echo(self):
        ret = connect_zerorpc('echo', """ '1', 2, 3, "4" """)
        assert ret == """ '1', 2, 3, "4" """

    @with_setup(setup_func, teardown_func)
    def test_01_help(self):
        connect_zerorpc('help')


class TestPyServerExecute:
    def setup(self):
        connect_zerorpc('execute', "set_root", self.TEST_URL)

    def teardown(self):
        pass

    def exploring(self):
        connect_zerorpc('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                        'noscript', 'comment', 'NavigableString')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '3')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '3')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')

    TEST_URL = "http://bbs.ruliweb.com/best/humor?&page=1"

    def test_01_set_url(self):
        connect_zerorpc('execute', "set_root", self.TEST_URL,print_=True)

    @with_setup(setup, teardown)
    def test_02_current_html(self):
        connect_zerorpc('execute', 'current_html')

    @with_setup(setup, teardown)
    def test_03_children_tag(self):
        connect_zerorpc('execute', 'children_tag')

    @with_setup(setup, teardown)
    def test_04_set_filter(self):
        connect_zerorpc('execute', 'children_tag')

        before = connect_zerorpc('execute', 'set_filter', 'head')

        after = connect_zerorpc('execute', 'children_tag')

        assert before != after

    @with_setup(setup, teardown)
    def test_05_move_down(self):
        before = connect_zerorpc('execute', 'children_tag')

        connect_zerorpc('execute', 'move_down', '7')

        after = connect_zerorpc('execute', 'children_tag')

        assert before != after

    @with_setup(setup, teardown)
    def test_06_move_up(self):
        # before
        connect_zerorpc('execute', 'move_up')

        # after
        connect_zerorpc('execute', 'children_tag')

    @with_setup(setup, teardown)
    def test_07_trace_stack(self):
        # connect_zerorpc('execute', 'set_filter', 'head', 'script', 'header', 'footer',
        #                 'noscript', 'comment', 'NavigableString')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')

    @with_setup(setup, teardown)
    def test_08_exploring(self):
        connect_zerorpc('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                        'noscript', 'comment', 'NavigableString')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '7')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '3')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '5')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '1')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')
        connect_zerorpc('execute', 'move_down', '3')

        connect_zerorpc('execute', 'trace_stack')
        connect_zerorpc('execute', 'children_tag')

    @with_setup(setup, teardown)
    def test_09_extract_current(self):
        self.test_08_exploring()
        connect_zerorpc('execute', 'extract_current', print_=True)

        connect_zerorpc('execute', 'extract_current', 'a', 'href',print_=True)

    @with_setup(setup, teardown)
    def test_10_export_parse_form(self):
        self.test_08_exploring()
        connect_zerorpc('execute', 'extract_current')
        connect_zerorpc('execute', 'extract_current', 'a', 'href')

        connect_zerorpc('execute', 'export_parse_form',print_=True)
        pass

    @with_setup(setup, teardown)
    def test_11_import_parse_form(self):
        self.test_08_exploring()
        parse_form = connect_zerorpc('execute', 'export_parse_form')
        connect_zerorpc('execute', 'import_parse_form', str(parse_form),print_=True)
        pass

    @with_setup(setup, teardown)
    def test_12_extract_from_parse_form(self):
        self.test_08_exploring()
        parse_form = connect_zerorpc('execute', 'export_parse_form',print_=True)
        connect_zerorpc('execute', 'import_parse_form', str(parse_form),print_=True)
        connect_zerorpc('execute', 'extract_from_parse_form', self.TEST_URL,print_=True)
        pass
