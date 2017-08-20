import inspect


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Chain(metaclass=Singleton):
    def __init__(self, enter=None, exit_=None):
        self.chain = {}
        self.enter = self.dummy
        self.exit = self.dummy

        if enter is not None:
            self.enter = enter
        if exit_ is not None:
            self.exit = exit_

    def chaining(self, *args):
        self.enter()

        # get caller's name
        fn_name = inspect.stack()[1][3]

        # resolve_chain chain
        # print('chaining resolve_chain', fn_name)
        # print(args)
        # print(self.chain)
        for chained_fn in args:
            if chained_fn is not None:
                chained_fn()
                # print(chained_fn.__name__)

        # hook chain
        if fn_name not in self.chain:
            # print('hook chain')
            # print('end chaining', fn.__name__)
            self.chain[fn_name] = args

            self.exit()

    @staticmethod
    def dummy():
        pass
