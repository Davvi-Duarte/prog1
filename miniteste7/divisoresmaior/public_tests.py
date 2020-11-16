import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_divisores_do_maior
        undertest = __import__(module)
        remove_divisores_do_maior = getattr(undertest, 'remove_divisores_do_maior', None)

    def test_exemplo(self):
        l1 = [6, 9, 10, 3, 5]
        assert  remove_divisores_do_maior(l1) == None
        assert l1 == [6, 9, 3]

    def test_exemplo2(self):
        l2 = [10, 20, 5, 24, 30]
        assert remove_divisores_do_maior(l2) == None
        assert l2 == [20, 24]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
