import unittest
from Clock import APIClock

class TestCommonMethods(object):
    clock = APIClock(self, )
    def setUp():
        pass
        #self.clock = APIClock

class TestTimeMethods(TestCommonMethods, unittest.TestCase):

    def setUp(self) -> None:
        return super()

    def test_getNextOpen(self):
        print(TestCommonMethods.clock.getNextOpen())
        self.assertEquals(1,1)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
