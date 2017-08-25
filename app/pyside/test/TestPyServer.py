import zerorpc

from main.BaseTest import BaseTest

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
    method = getattr(conn, cmd)
    ret = method(*args)
    conn.close()

    return ret


class TestPyServer(BaseTest):
    def test00_echo(self):
        args = ('echo', """ '1', 2, 3, "4" """)
        # ret = connect_zerorpc('echo', """ '1', 2, 3, "4" """)
        ret = connect_zerorpc(*args)
        self.log(ret)
        assert ret == """ '1', 2, 3, "4" """

    def test01_help(self):
        ret = connect_zerorpc('help')

        self.log(ret)

    def test02_echo_dict(self):
        ret = connect_zerorpc('echo_dict')
        self.log(ret)
