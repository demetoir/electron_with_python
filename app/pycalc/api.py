from __future__ import print_function
import zerorpc
import logging
from os import path


class Pyserver(object):
    def __init__(self):
        # cur_path = '/home/demetoir/WebstormProjects/electron_with_python/app/pycalc/pyserver_log.txt'
        self.log = logging.getLogger(self.__class__.__name__ + ' logger')
        cur_path = path.join(path.curdir, 'pyserver.log')
        self.log.basicConfig(filename=cur_path, level=logging.INFO)

        pass

    def __repr__(self):
        return self.__class__.__name__

    def echo(self, text):
        """echo any text"""
        self.log.info(text)
        return text

    def f(self, text, num, ):
        return "response %s %d" % (text, int(num))


def main():
    port = str(4242)
    addr = 'tcp://127.0.0.1:' + port
    s = zerorpc.Server(Pyserver())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()


if __name__ == '__main__':
    main()
