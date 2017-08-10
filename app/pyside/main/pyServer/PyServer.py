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
from types import *
from main.logger.logger import Logger
from main.tagExplorer.TagExplorer import TagExplorer as txp
from main.util.util import *


class PyServer:
    """zerorpc based python server for TagExplorer"""

    def __init__(self):
        self.log = Logger(self.__class__.__name__).log
        self.txp = txp()
        pass

    def __repr__(self):
        return self.__class__.__name__

    def echo(self, text):
        """
        echo any text

        :param text : str

        :return: str
        """
        self.log.info(text)
        return text

    def help(self):
        """
        echo TagExplorer instance's function list

        :return: list
        """
        msg = """txp cmd list \n"""
        for attr in txp.__dict__:
            if type(getattr(txp, attr)) is FunctionType:
                msg += attr + " "
        return msg

    def execute(self, cmd, *args):
        """
        execute TagExplorer instance

        :param cmd: str
        :param args: *args
        :return: executed cmd result
        """
        # type mapping
        args = tuple(map(argsMapper, args))

        ret = None
        if hasattr(txp, cmd):
            method = getattr(self.txp, cmd)
            self.log.info(self.txp.__class__.__name__ + ' execute cmd : %s args : %s' % (cmd, argsToStr(args)))
            try:
                ret = method(*args)
            # TODO need exception filtering more
            except Exception as e:
                self.log.error(e)
                msg = self.txp.__class__.__name__ + " execute fail, cmd %s args %s does not match" % (
                    cmd, argsToStr(args))
                self.log.error(msg)
                return msg
            finally:
                return ret
        else:
            msg = self.txp.__class__.__name__ + ' can not execute %s' % cmd
            self.log.error(msg)
            return msg

    def info(self):
        """
        return infomation of txp instance
        curent target url and filer list

        :return: list
        """
        url = self.txp.url
        filter_list = self.txp.filter_list
        return url, filter_list


DEFAULT_PORT = str(4242)
DEFAULT_ADDRESS = 'tcp://127.0.0.1'


def main():
    addr = DEFAULT_ADDRESS + ":" + DEFAULT_PORT
    print('zerorpc ' + addr)
    server = zerorpc.Server(PyServer())
    server.bind(addr)
    print('start running on {}'.format(addr))
    server.run()

    # TODO pack and unpack packet by json
    # todo test all... please


if __name__ == '__main__':
    main()
