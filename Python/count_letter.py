import unittest

def count_letter(words, letter_for_count):
    return words.count(letter_for_count)

class CountLetterTest(unittest.TestCase):
    def test_input_Hello_World_and_l_return_3(self):
        actual = count_letter("Hello World", "l")
        expected = 3
        self.assertEqual(expected, actual)

    def test_input_Hello_World_and_o_return_2(self):
        actual = count_letter("Hello World", "o")
        expected = 2
        self.assertEqual(expected, actual)

    def test_input_aa11bb22cc33_and_b_return_2(self):
        actual = count_letter("aa11bb22cc33", "b")
        expected = 2
        self.assertEqual(expected, actual)
    
    def test_input_ocean_blue_and_m_return_0(self):
        actual = count_letter("ocean blue", "m")
        expected = 0
        self.assertEqual(expected, actual)

    def test_input_coffee_or_tea_and_f_return_2(self):
        actual = count_letter("coffee or tea", "f")
        expected = 2
        self.assertEqual(expected, actual)
    
    def test_input_banana_and_b_return_1(self):
        actual = count_letter("banana", "b")
        expected = 1
        self.assertEqual(expected, actual)

unittest.main()