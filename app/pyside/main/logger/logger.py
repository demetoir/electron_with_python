# util
import logging
import logging.handlers
from os import path
import os
import sys
import inspect

# http://ourcstory.tistory.com/97
# http://ourcstory.tistory.com/105
# TODO more comment
ENDL = '\n'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    LOG_FOLDER_NAME = 'log'
    LOG_PATH = path.join('.', LOG_FOLDER_NAME)
    INFO = 0

    LOG_FORMAT = '[%(levelname)s | %(filename)s:%(lineno)s] %(asctime)s > %(message)s'
    LOG_SIMPLE_FORMAT = '> %(message)s'

    def __init__(self, logger_name, stdout_only=False, simple=False):
        self.log = logging.getLogger(logger_name)
        self.log.setLevel(logging.DEBUG)

        if simple:
            formatter = logging.Formatter(self.LOG_SIMPLE_FORMAT)
        else:
            formatter = logging.Formatter(self.LOG_FORMAT)

        if stdout_only:
            # add stdout handler
            self.stream_handler = logging.StreamHandler(sys.stdout)
            self.stream_handler.setFormatter(formatter)
            self.log.addHandler(self.stream_handler)
            pass
        else:
            # make dir for log path
            if not path.exists(self.LOG_PATH):
                os.makedirs(self.LOG_PATH)
            self.LOG_FULL_PATH = path.join(self.LOG_PATH, self.LOG_FOLDER_NAME)

            # add file handler
            self.file_handler = logging.FileHandler(self.LOG_FULL_PATH)
            self.file_handler.setFormatter(formatter)
            self.log.addHandler(self.file_handler)

        self._is_enable = True

    def var_log(self, var):
        if self._is_enable:
            st = inspect.stack()[1]
            line_num = st[2]
            call_f = st[3]
            code = " ".join(st[4][0].split())
            var_name = code.replace('self.log(', '')[:-1]
            msg = ''
            try:
                msg += '%s(%s) | %s : %s\n' % (call_f, line_num, var_name, str(type(var)))

                if type(var) is str:
                    msg += str(var) + ENDL
                elif type(var) is dict:
                    l = [str(k) + ' : ' + str(var[k]) for k in var]
                    msg += '{' + ',\n'.join(l) + '}'
                else:
                    msg += '[' + ',\n'.join(map(str, var)) + ']' + ENDL

            except Exception as e:
                msg += str(var) + ENDL
            finally:
                self.log.log(level=logging.DEBUG, msg=msg, )

    def disable(self):
        self._is_enable = False

    def enable(self):
        self._is_enable = True
