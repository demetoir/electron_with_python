import pdb

def f_a():
    a = 1
    print('f_a', locals())


def f_b():
    b = 1
    f_a()

    print('f_b', locals())
    print('f_b g', globals())


class A:
    def __init__(self):
        print('call init')
        self._x = None

    def __new__(cls, *args, **kwargs):
        print('call new')
        return super().__new__(cls)

    def x_setter(self, value):
        print('setter')
        self._x = value

    def x_getter(self):
        print('getter')
        return self._x

    x = property(x_getter, x_setter)


def test():
    a = A()

    print(a)
    print(a.x)
    a.x = 3
    print(a.x)

    print(id(a))
#    TODO....... this is paaaaaaaaaaaaaaaiiiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnn


if __name__ == '__main__':
    pdb.run('test()')

