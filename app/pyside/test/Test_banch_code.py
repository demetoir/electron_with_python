from nose import with_setup


class TestClass:
    def __init__(self):
        self.state = 0

    def setup_f(self):
        print('setup')
        pass

    @staticmethod
    def teardown_f():
        print('teardown')
        pass

    def test_00000_class_setup(self):
        print('class setup')
        self.state = 0

        pass

    def test_99999_class_teardown(self):
        print('class teardown')
        self.state = -1
        pass

    @with_setup(setup_f, teardown_f)
    def test_01(self):
        self.state = 1
        print('test_01, state = ', self.state)

    @with_setup(setup_f, teardown_f)
    def test_02(self):
        self.state = 2
        print('test_02, state = ', self.state)
