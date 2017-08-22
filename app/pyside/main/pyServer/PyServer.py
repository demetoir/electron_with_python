"""add PyServer directory to system path"""
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
import traceback
from types import *
from main.logger.logger import Logger
from main.tagExplorer.TagExplorer import TagExplorer as txp
from main.util.util import *


class PyServer:
    """zerorpc based python server for TagExplorer"""
    DEFAULT_PORT = str(4242)
    DEFAULT_ADDRESS = 'tcp://127.0.0.1'
    DEFAULT_FULL_ADDRESS = DEFAULT_ADDRESS + ":" + DEFAULT_PORT

    def __init__(self):
        self.log = Logger(self.__class__.__name__).log
        self.txp = txp()
        pass

    def __repr__(self):
        return self.__class__.__name__

    def echo(self, text):
        self.log.info(text)
        return text

    def help(self):
        """
        echo TagExplorer instance's function list

        :return: list
        """
        ret = []
        for attr in txp.__dict__:
            if type(getattr(txp, attr)) is FunctionType:
                ret += [attr]
        ret.sort()
        return ret

    def execute(self, cmd, *args):
        """
        execute TagExplorer instance

        :param cmd: str
        :param args: *args
        :return: executed cmd result
        """
        # type mapping
        ret = None
        try:
            args = tuple(map(argsMapper, args))
            method = getattr(self.txp, cmd)
            self.log.info('execute cmd : %s args : %s' % (cmd, argsToStr(args)))
            ret = method(*args)

        except Exception as e:
            msg = 'can not execute cmd : %s, args : %s' % (cmd, argsToStr(args)) + "\n" \
                  + str(e) \
                  + "\n" + str(traceback.format_exc())
            self.log.error(msg)
            ret = msg

        finally:
            # todo delete yield
            # not_yield_ret = []
            # for item in ret:
            #     not_yield_ret += [item]

            return ret

    def execute_many(self, *args):
        # tODO need?
        pass

    def info(self):
        """
        return information of txp instance
        current target url and filer list

        :return: list
        """
        url = self.txp.url
        filter_list = self.txp.filter_list
        return url, filter_list


def main():
    addr = PyServer.DEFAULT_FULL_ADDRESS
    print('zerorpc ' + addr)
    server = zerorpc.Server(PyServer())
    server.bind(addr)
    print('start running on {}'.format(addr))
    server.run()

    # todo test all... please


if __name__ == '__main__':
    main()
