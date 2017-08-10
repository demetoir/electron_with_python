from nose import with_setup
from types import *
from main.tagExplorer.HardParser import HardParser
from main.tagExplorer.TagExplorer import TagExplorer
from main.util import util
from main.tagExplorer.Tag import Tag

URL_SITE = """http://bbs.ruliweb.com/best/humor?&page=%d"""


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_00_setup():
    return


@with_setup(setup_func, teardown_func)
def test_99_teardown():
    return

@with_setup(setup_func, teardown_func)
def test_01_():
    url = 'http://bbs.ruliweb.com/best/humor'
    filter_list = ['head', 'script', 'header', 'footer', 'noscript']
    txp = TagExplorer()
    txp.set_url(url)
    txp.set_filter(filter_list)



    for i in TagExplorer.__dict__:
        print(i, type(getattr(TagExplorer, i)), type(getattr(TagExplorer, i)) is FunctionType)


@with_setup(setup_func, teardown_func)
def test_02_work():
    url = 'http://bbs.ruliweb.com/best/humor'
    filter_list = ['head', 'script', 'header', 'footer', 'noscript']
    txp = TagExplorer()
    txp.set_url([url])
    txp.set_filter(filter_list)

    while True:
        util.open_web(txp.current_html())

        for tag in txp.children_tag():
            print(tag)

        s = str(input())

        if s.isnumeric():
            txp.move_down(int(s))
        elif s is 'b':
            txp.move_up()
        else:
            break

    for item in txp.trace_stack():
        print(item)
