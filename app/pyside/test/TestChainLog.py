from main.BaseTest import BaseTest


class TestChainLog(BaseTest):
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

    def test_chain_deco2(self):
        print('test deco chain 2')
        # self.log(2)

    def test_chain_deco3(self):
        print('test deco chain 3')
        # self.log(3)


class TestChild(BaseTest):
    def test_child_chain1(self):
        self.chaining(None)
        print('child chain test 1')
        self.log(-1)

    def test_child_chain2(self):
        self.chaining(self.test_child_chain1())
        print('child chain test 2')
        a = float
        self.log(-2)
        self.log(a)
