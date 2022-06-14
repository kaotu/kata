import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_return_Fizz(self):
        actual = fizz_buzz(3)
        expected = "Fizz"
        self.assertEqual(expected, actual)

    def test_input_5_return_Buzz(self):
        actual = fizz_buzz(5)
        expected = "Buzz"
        self.assertEqual(expected, actual)
    
    def test_input_15_return_Fizz(self):
        actual = fizz_buzz(15)
        expected = "FizzBuzz"
        self.assertEqual(expected, actual)

    def test_input_10_return_Buzz(self):
        actual = fizz_buzz(10)
        expected = "Buzz"
        self.assertEqual(expected, actual)
    
    def test_input_1_return_1(self):
        actual = fizz_buzz(1)
        expected = 1
        self.assertEqual(expected, actual)
        
    def test_input_0_return_0(self):
        actual = fizz_buzz(0)
        expected = 0
        self.assertEqual(expected, actual)


def fizz_buzz(number):
    if number == 0:
        return 0
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    return number


unittest.main()