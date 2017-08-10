import os
import shutil
import webbrowser

from main.db.DbContract import *


def clean_up():
    if os.path.exists(DBContract.DB_PATH):
        shutil.rmtree(DBContract.DB_PATH)


def print_rows(rows):
    print('total = %d' % len(rows))
    for row in rows:
        print(row)
    print()


def print_parse_items(items):
    for item in items:
        print(item)


def print_soup_children(soup):
    for i, child in enumerate(soup.__children):
        if child.name is None:
            continue
        print(i, child.name, child.attrs)
    print()


def open_web(html):
    """opening web page by string type html """
    file_name = 'punning_html.html'
    full_path = os.path.join(os.path.curdir, file_name)
    with open(full_path, 'wb') as f:
        f.write(html.encode('utf-8'))

    webbrowser.open_new_tab(full_path)


def argsToStr(*args):
    return " ".join(map(str, args))


def isFloat(s):
    try:
        float(s)
    except Exception as e:
        return False
    return True


def isInt(s):
    try:
        int(s)
    except Exception as e:
        return False
    return True


def argsTypeMapping(*args):
    ret = []
    for arg in args:
        if isInt(arg):
            ret += [int(arg)]
        elif isFloat(arg):
            ret += [float(arg)]
        else:
            ret += [arg]
    return ret


def argsMapper(arg):
    if isInt(arg):
        ret = int(arg)
    elif isFloat(arg):
        ret = float(arg)
    else:
        ret = str(arg)
    return ret


if __name__ == '__main__':
    i = ['1', '2', '"3"', '6.5']
    out = list(map(argsMapper, i))

    print(out)
    for i in out:
        print(i, type(i))

    pass
