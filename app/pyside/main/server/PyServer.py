# add pyside dir
try:
    import os
    import sys

    path = os.path.abspath(__file__)
    path = path.split(os.sep)
    path = path[:path.index('pyside') + 1]
    sys.path.append(os.sep.join(path))

    del os
    del sys
except Exception as e:
    print(e)
    exit(-1)

import zerorpc
from main.logger.logger import Logger
from main.htmlTagExplorer.htmlTagExplorer import HtmlTagExplorer as txp

DEFAULT_PORT = str(4242)
DEFAULT_ADDRESS = 'tcp://127.0.0.1'


class PyServer():
    def __init__(self):
        self.log = Logger(self.__class__.__name__).log
        self.txp = txp()
        pass

    def __repr__(self):
        return self.__class__.__name__

    def echo(self, text):
        """echo any text"""
        self.log.info(text)
        return text

    def f(self, text, num, ):
        """test f function"""
        return "response %s %d" % (text, int(num))

    def set_target_address(self, address):
        """set address"""
        self.txp.__root__(address)
        return "address set"


def main():
    addr = DEFAULT_ADDRESS + ":" + DEFAULT_PORT
    print('zerorpc ' + addr)
    server = zerorpc.Server(PyServer())
    server.bind(addr)
    print('start running on {}'.format(addr))
    server.run()


if __name__ == '__main__':
    main()
