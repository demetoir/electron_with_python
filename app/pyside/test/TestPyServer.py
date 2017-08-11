from nose import with_setup
import subprocess
import time
import zerorpc
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


def connect_zerorpc(cmd, *args):
    conn = zerorpc.Client()
    conn.connect("tcp://127.0.0.1:4242")

    print('cmd : %s , args : %s ' % (cmd, argsToStr(args)))

    method = getattr(conn, cmd)
    ret = method(*args)

    conn.close()
    if type(ret) is list:
        for i in ret:
            print(i)
    else:
        print(ret)
    print()

    return ret

def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_00_connection_test():
    pass
    connect_zerorpc('echo', """ '1', 2, 3, "4" """)


@with_setup(setup_func, teardown_func)
def test_01_help():
    connect_zerorpc('help')


@with_setup(setup_func, teardown_func)
def test_02_set_url():
    connect_zerorpc('execute', "set_url", "http://bbs.ruliweb.com/best/humor?&page=1")


@with_setup(setup_func, teardown_func)
def test_03_current_html():
    connect_zerorpc('execute', 'current_html')


@with_setup(setup_func, teardown_func)
def test_04_children_tag():
    connect_zerorpc('execute', 'children_tag')


@with_setup(setup_func, teardown_func)
def test_05_set_filter():
    # before
    connect_zerorpc('execute', 'children_tag')

    connect_zerorpc('execute', 'set_filter', 'head')

    # after
    connect_zerorpc('execute', 'children_tag')


@with_setup(setup_func, teardown_func)
def test_06_move_down():
    connect_zerorpc('execute', 'children_tag')

    connect_zerorpc('execute', 'move_down', '7')

    connect_zerorpc('execute', 'children_tag')


@with_setup(setup_func, teardown_func)
def test_07_move_up():
    # before
    connect_zerorpc('execute', 'move_up')

    # after
    connect_zerorpc('execute', 'children_tag')


@with_setup(setup_func, teardown_func)
def test_08_trace_stack():
    connect_zerorpc('execute', "set_url", "http://bbs.ruliweb.com/best/humor?&page=1")
    connect_zerorpc('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                    'noscript', 'comment', 'NavigableString')

    connect_zerorpc('execute', 'trace_stack')
    connect_zerorpc('execute', 'children_tag')
    connect_zerorpc('execute', 'move_down', '7')

    connect_zerorpc('execute', 'trace_stack', )
    connect_zerorpc('execute', 'children_tag')

    connect_zerorpc('execute', 'move_down', '5')

    connect_zerorpc('execute', 'trace_stack')
    connect_zerorpc('execute', 'children_tag')

    connect_zerorpc('execute', 'move_down', '7')

    connect_zerorpc('execute', 'trace_stack')

    connect_zerorpc('execute', 'children_tag')
