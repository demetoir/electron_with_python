from nose import with_setup
from main.tagExplorer.TagExplorer import TagExplorer
from main.util.util import *
import sys

URL_SITE = """http://bbs.ruliweb.com/best/humor?&page=%d"""

# test resource
TEST_URL = "http://bbs.ruliweb.com/best/humor?&page=1"

ENDL = '\n'
is_logging = True
txp = None


def log(var):
    global is_logging
    if is_logging:
        try:
            sys.stdout.write(str(type(var)) + ENDL)
            if type(var) is str:
                sys.stdout.write(str(var) + ENDL)
            else:
                for item in var:
                    sys.stdout.write(str(item) + ENDL)
        except Exception as e:
            print(e)
        finally:
            print()


def setup_f(fn):
    def wrapped():
        print('setup_f', fn.__name__)
        global is_logging, txp
        is_logging = False
        ret = fn()
        txp = ret
        is_logging = True

        return ret

    return wrapped


def setup():
    pass


def teardown():
    global txp
    txp = None
    print('teardown')
    pass


def exploring():
    # connect_zerorpc('execute', 'set_filter', 'head', 'script', 'header', 'footer',
    #                 'noscript', 'comment', 'NavigableString')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '7')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '5')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '7')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '7')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '1')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '3')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '1')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '5')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '1')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '5')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '1')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    # connect_zerorpc('execute', 'move_down', '3')
    #
    # connect_zerorpc('execute', 'trace_stack')
    # connect_zerorpc('execute', 'children_tag')
    pass


def set_filter(txp, *args):
    txp.set_filter(*args)
    return txp


@with_setup(setup, teardown)
def test_00_init():
    txp = TagExplorer()

    return txp


@with_setup(setup, teardown)
def test_01_set_root():
    txp = test_00_init()
    txp.set_root(TEST_URL)

    # todo ....
    assert True

    return txp


@with_setup(setup, teardown)
def test_02_current_html():
    txp = test_01_set_root()
    ret = txp.current_html()

    assert True

    return txp


@with_setup(setup, teardown)
def test_03_children_tag():
    txp = test_01_set_root()
    ret = txp.children_tag()
    log(ret)

    assert True

    return txp


@with_setup(setup, teardown)
def test_04_set_filter():
    txp = test_01_set_root()

    before = txp.children_tag()

    txp.set_filter('comment')

    after = txp.children_tag()

    log(before)
    log(after)

    assert before != after

    return txp


@with_setup(setup_f(test_01_set_root), teardown)
def test_05_move_down():
    global txp

    before = txp.children_tag()

    txp.move_down(7)

    after = txp.children_tag()

    log(before)
    log(after)

    assert before != after
    return txp


@with_setup(setup_f(test_01_set_root), teardown)
def test_06_move_up():
    global txp

    txp.move_down(7)
    before = txp.children_tag()

    txp.move_up()

    after = txp.children_tag()

    log(before)
    log(after)

    assert before != after
    return txp


@with_setup(setup_f(test_01_set_root), teardown)
def test_07_trace_stack():
    global txp
    txp.set_filter('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                   'noscript', 'comment', 'NavigableString')

    before = txp.trace_stack()
    txp.children_tag()
    txp.move_down(7)
    txp.trace_stack()

    after = txp.trace_stack()
    txp.children_tag()

    log(before)
    log(after)

    assert before != after
    return txp


@with_setup(setup_f(test_01_set_root), teardown)
def test_08_exploring():
    global txp
    txp.set_filter('execute', 'set_filter', 'head', 'script', 'header', 'footer',
                   'noscript', 'comment', 'NavigableString')

    move_down_list = [7, 5, 7, 7, 1, 3, 1, 5, 1, 5, 1, 3]
    for idx in move_down_list:
        trace_stack = txp.trace_stack()
        children_tag = txp.children_tag()
        txp.move_down(idx)
        log(trace_stack)
        log(children_tag)

    trace_stack = txp.trace_stack()
    log(trace_stack)
    children_tag = txp.children_tag()
    log(children_tag)

    ret = txp.current_html()
    log(ret)

    return txp


@with_setup(setup_f(test_08_exploring), teardown)
def test_09_extract_current():
    global txp

    ret = txp.extract_current()
    log(ret)

    ret = txp.extract_current('a', 'href')
    log(ret)

    return txp


@with_setup(setup_f(test_09_extract_current), teardown)
def test_10_export_parse_form():
    global txp
    ret = txp.export_parse_form()
    log(ret)
    return txp


@with_setup(setup_f(test_09_extract_current), teardown)
def test_11_import_parse_form():
    global txp
    parse_form = txp.export_parse_form()
    log(parse_form)
    parse_form = str(parse_form)

    txp.import_parse_form(parse_form)

    return txp


@with_setup(setup_f(test_11_import_parse_form), teardown)
def test_12_extract_from_parse_form():
    global txp
    ret = txp.extract_from_parse_form(TEST_URL)
    log(ret)
    pass
