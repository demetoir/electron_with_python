from main.Chain import Chain
from main.logger.logger import Logger


def deco(fn):
    def wrapped():
        print('deco')
        return fn()

    return wrapped

class TestChainLog:
    logger = None
    log = None
    chain = None
    chaining = None

    def setup(self):
        self.logger = Logger(TestChainLog.__name__, stdout_only=True, simple=True)
        self.log = self.logger.var_log

        self.chain = Chain(enter=self.logger.disable, exit_=self.logger.enable)
        self.chaining = self.chain.chaining
        print('setup')

        # # below method any one work so i use singleton or global variable
        # @classmethod
        # def setupClass(cls):
        #     print('setupClass')
        #
        # @classmethod
        # def setUpClass(cls):
        #     print('setUpClass')
        #
        # @classmethod
        # def setupAll(cls):
        #     print('setupAll')
        #
        # @classmethod
        # def setUpAll(cls):
        #     print('selfUpAll')
        #
        # @classmethod
        # def setup_class(cls):
        #     """This method is run once for each class before any tests are run"""
        #     print('class  setup')
        #
        # @classmethod
        # def teardown_class(cls):
        #     """This method is run once for each class _after_ all tests are run"""
        #     print('class teardown')

    def teardown(self):
        print('teardown')
        self.chain = None
        self.chaining = None

    def __init__(self):
        self.chain = None
        self.chaining = None

    def test_chain1(self):
        self.chaining(None, None)
        print('test chain 1')
        self.log(1)

    def test_chain2(self):
        self.chaining(self.test_chain1)
        print('test chain 2')
        self.log(2)

    def test_chain3(self):
        self.chaining(self.test_chain2)
        print('test chain 3')
        self.log(3)

    def test_chain4(self):
        self.chaining(None)
        print('test chain 4')
        self.log(4)

    def test_chain5(self):
        self.chaining(self.test_chain4)
        print('test chain 5')
        self.log(5)

    def test_chain6(self):
        self.chaining(self.test_chain3, self.test_chain5)
        print('test chain 6')
        self.log(6)

    def test_logger(self):
        a = 1
        s = 'ssss'
        l = [i for i in range(10)]
        self.log(a)
        self.log(s)
        self.log(l)

    def test_chain_deco1(self):
        self.chaining(None)
        print('test deco chain 1')
        self.log(1)

    @deco
    def test_chain_deco2(self):
        print('test deco chain 2')
        self.log(2)

    @deco
    def test_chain_deco3(self):
        print('test deco chain 3')
        self.log(3)
