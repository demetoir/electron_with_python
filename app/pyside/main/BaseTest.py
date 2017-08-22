from main.Chain import Chain
from main.logger.logger import Logger


class BaseTest:
    logger = None
    log = None
    chain = None
    chaining = None

    def setup(self):
        self.logger = Logger(self.__class__.__name__, stdout_only=True, simple=True)
        self.log = self.logger.var_log

        self.chain = Chain(enter=self.logger.disable, exit_=self.logger.enable)
        self.chaining = self.chain.chaining
        # print('setup')

    def teardown(self):
        # print('teardown')
        self.chain = None
        self.chaining = None

    def __init__(self):
        self.chain = None
        self.chaining = None
