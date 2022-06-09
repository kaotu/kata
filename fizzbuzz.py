import unittest



class FizzBuzz(unittest.TestCase):
    def test_input_3_return_Fizz(self):
        actual = fizz_buzz(3)
        expected = "Fizz"
        self.assertEqual(actual, expected)
        
    def test_input_5_return_Buzz(self):
        actual = fizz_buzz(5)
        expected = "Buzz"
        self.assertEqual(actual, expected)

    def test_input_2_return_Fizz(self):
        actual = fizz_buzz(2)
        expected = 2
        self.assertEqual(actual, expected)


def fizz_buzz(number):
    if number == 5:
        return "Buzz"
    if number == 2:
        return "Fizz"
    
    return "Fizz"
    
unittest.main()