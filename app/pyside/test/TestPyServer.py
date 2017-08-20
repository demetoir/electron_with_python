import zerorpc
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


def setup():
    print('setup')
    pass


def teardown():
    print('teardown')
    pass


@with_setup(setup, teardown)
def test_00_echo():
    ret = connect_zerorpc('echo', """ '1', 2, 3, "4" """)
    assert ret == """ '1', 2, 3, "4" """


@with_setup(setup, teardown)
def test_01_help():
    connect_zerorpc('help')