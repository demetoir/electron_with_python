def add(a, b):
    print('in add', a, b)
    return a + b


def f(func, *args):
    print('in f', *args)
    return func(*args)


def no_param():
    print('in s')
    return 0


if __name__ == '__main__':
    a = (1, 2)
    f(add, *a)
    f(no_param, *())
    f(no_param, *(1, 2, 3))

    s = 'ssss     sd s s s s s'
    print(s)
    print(str(s))
    print(s.isspace())

    #
    # parser = Parser()
    #
    # items = []
    # for i in range(1, 2 + 1):
    #     res = parser.parse_ruliweb(URL_SITE % i)
    #     items += res
    #
    # items.sort(key=lambda item: item[NewFeedContract.KW_URL])
    #
    # db_helper = DbHelper()
    # table_name = NewFeedContract.TABLE_NAME
    #
    # res = db_helper.insert_items(table_name, items)
    #
    # rows = db_helper.query_all(table_name)
