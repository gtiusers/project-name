from caculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("start test")

    def test_add(self):
        j=Math(7,10)
        self.assertEqual(j.add(),15)
        #self.assertEqual(j.add(),12)

    def tearDown(self):
        print("test end")

if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(TestMath("test_add"))

    runner=unittest.TextTestRunner()
    runner.run(suit)
