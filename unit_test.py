import unittest
from modules.module1 import Module1
from modules.module2 import Module2
from modules.module3 import Module3


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.module1 = Module1()
        self.module2 = Module2()
        self.module3 = Module3()

    # Unit test for module 1
    def test_substract_module1(self):
        print('test_substract_module1')
        self.assertEqual(self.module1.substract_num(num1=1, num2=2), -1)
        self.assertEqual(self.module1.substract_num(num1=3, num2=10), -7)
        self.assertEqual(self.module1.substract_num(num1=20, num2=15), 5)

    def test_get_length_module1(self):
        print('test_get_length_module1')
        self.assertEqual(self.module1.get_length(arr=[]), 0)
        self.assertEqual(self.module1.get_length(arr=[1, 2, 3]), 3)
        self.assertEqual(self.module1.get_length(arr=[1, 2, 3, 4, 5]), 5)

    def test_check_array_module1(self):
        print('test_get_length_module1')
        self.assertEqual(self.module1.check_array(arr=[]), [])
        self.assertEqual(self.module1.check_array(arr=[1, 2, 3]), [3])
        self.assertEqual(self.module1.check_array(arr=[1, 2, 3, 4, 5]), [5])

    # Unit test for module 2
    def test_devide_num_module2(self):
        print('test_devide_module2')
        self.assertEqual(self.module2.devide_num(num1=1, num2=2), 0.5)
        self.assertEqual(self.module2.devide_num(num1=3, num2=10), 0.3)
        self.assertEqual(self.module2.devide_num(num1=20, num2=4), 5)

        with self.assertRaises(ValueError):
            self.module2.devide_num(num1=10, num2=0)

    def test_get_length_module2(self):
        print('test_get_length_module2')
        self.assertEqual(self.module2.get_length(arr=[]), 0)
        self.assertEqual(self.module2.get_length(arr=[1, 2, 3]), 3)
        self.assertEqual(self.module2.get_length(arr=[1, 2, 3, 4, 5]), 5)

    def test_check_array_module2(self):
        print('test_get_length_module2')
        self.assertEqual(self.module2.check_array(arr=[],
                                                  num=1), [])
        self.assertEqual(self.module2.check_array(arr=[1, 2, 3],
                                                  num=3), [3])
        self.assertEqual(self.module2.check_array(arr=[1, 2, 3, 4, 5],
                                                  num=2), [2, 4])

    # Unit test for module 3
    def test_parse_string_module3(self):
        print('test_parse_string_module3')
        self.assertEqual(self.module3.parse_string(string=""),
                         [''])
        self.assertEqual(self.module3.parse_string(string="a b c d e f "),
                         ['a', 'b', 'c', 'd', 'e', 'f', ''])
        self.assertEqual(self.module3.parse_string(string="souvenir loud four lost"),
                         ['souvenir', 'loud', 'four', 'lost'])

    def test_get_length_module3(self):
        print('test_get_length_module3')
        self.assertEqual(self.module3.get_length(string="abc"), 3)
        self.assertEqual(self.module3.get_length(string="abcd"), 4)

    def test_is_word_valid_module3(self):
        print('test_is_word_valid_module3')
        self.assertEqual(self.module3.is_word_valid(string="abc"), True)
        self.assertEqual(self.module3.is_word_valid(string="abcd"), True)
        self.assertEqual(self.module3.is_word_valid(string=""), False)

    def test_check_string_module3(self):
        print('test_check_string_module3')
        self.assertEqual(self.module3.check_string(string="souvenir loud four lost", num=4),
                         ['loud', 'four', 'lost'])
        self.assertEqual(self.module3.check_string(string="test is tests", num=2),
                         ['is'])
        self.assertEqual(self.module3.check_string(string="this is a word   ", num=1),
                         ['a'])


if __name__ == '__main__':
    unittest.main()
