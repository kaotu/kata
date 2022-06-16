import unittest

def count_letter(words, input):
	count = 0
	for word in words:
		if word == input:
			count += 1
	return count

class CountLetterTest(unittest.TestCase):
	def test_input_Hello_World_and_l_return_3(self):
		actual = count_letter("Hello World", "l")
		expected = 3
		self.assertEqual(expected, actual)

	def test_input_Hello_World_and_o_return_2(self):
		actual  = count_letter("Hello World", "o")
		expected = 2
		self.assertEqual(expected, actual)

	def test_input_Hello_World_and_r_return_1(self):
		actual = count_letter("Hello World", "r")
		expected = 1
		self.assertEqual(expected, actual)

	def test_input_Hello_World_and_W_return_1(self):
		actual = count_letter("Hello World", "W")
		expected = 1
		self.assertEqual(expected, actual)

	def test_input_Craft_Coffee_and_C_return_2(self):
		actual = count_letter("Craft Coffee", "C")
		expected = 2
		self.assertEqual(expected, actual)

unittest.main()