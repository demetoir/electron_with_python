from nose import with_setup
import subprocess
import time

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


def spawn_process(query_cmd=None):
    p = subprocess.Popen(
        query_cmd,
        stdout=subprocess.PIPE)

    ret = str(p.stdout.readline(), 'utf-8')

    while True:
        # line = str(p.stdout.readline(), 'utf-8')[2:-3]
        line = str(p.stdout.readline(), 'utf-8')
        if line == "":
            break
        ret += line.replace("'", "")
        time.sleep(0.0001)

    p.terminate()

    return ret


def setup_func():
    pass


def teardown_func():
    pass


cmds = [

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'current_html'],

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'set_filter', 'script', 'header', 'footer',
     'noscript'],
    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'current_html'],

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'set_filter', 'head', 'script', 'header', 'footer',
     'noscript'],

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'set_filter', 'head', 'script', 'header', 'footer',
     'noscript', 'comment', 'NavigableString'],

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag'],
    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'move_down', '5'],

    ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag'],

]


@with_setup(setup_func, teardown_func)
def test_00_connection_test():
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_01_help():
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'help']
    ret = spawn_process(query_cmd=cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_02_set_url():
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'set_url', "http://bbs.ruliweb.com/best/humor?&page=1"]
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_03_current_html():
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'current_html']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_04_children_tag():
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_05_set_filter():
    # before
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)

    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'set_filter', 'head']
    ret = spawn_process(cmd)
    print(ret)

    # after
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_06_move_down():
    # before
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)

    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'move_down', '7']
    ret = spawn_process(cmd)
    print(ret)

    # after
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_07_move_up():
    # before
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)

    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'move_up', ]
    ret = spawn_process(cmd)
    print(ret)

    # after
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'children_tag']
    ret = spawn_process(cmd)
    print(ret)


@with_setup(setup_func, teardown_func)
def test_08_trace_stack():
    # before
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'trace_stack', ]
    ret = spawn_process(cmd)
    print(ret)

    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'move_down', '7']
    ret = spawn_process(cmd)
    print(ret)

    # after
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'trace_stack', ]
    ret = spawn_process(cmd)
    print(ret)
    # cleanup
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'execute', 'move_up', ]
    ret = spawn_process(cmd)
    print(ret)
