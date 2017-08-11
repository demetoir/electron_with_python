import zerorpc
from main.util.util import *


def connect_zerorpc(cmd, *args):
    conn = zerorpc.Client()
    conn.connect("tcp://127.0.0.1:4242")

    print('cmd : %s , args : %s ' % (cmd, argsToStr(args)))

    method = getattr(conn, cmd)
    ret = method(*args)

    conn.close()
    if ret is not None:
        for i in ret:
            print(i)
    else:
        print(ret)
    print()

    return ret


if __name__ == '__main__':
    connect_zerorpc('echo', ('1', 2, 3, "4"))
    connect_zerorpc('execute', "set_url http://bbs.ruliweb.com/best/humor?&page=1")
    connect_zerorpc('execute', "set_filter", "head")
    connect_zerorpc('execute', "children_tag")
    pass
