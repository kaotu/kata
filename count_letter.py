import unittest

class CountLetter(unittest.TestCase):
	def test_input_Hello_World_and_o_return_2(self):
		actual = count_letter("Hello World", "o")
		expected = 2
		self.assertEqual(expected, actual)
  
	def test_input_Hello_World_and_l_return_3(self):
		actual = count_letter("Hello World", "l")
		expected = 3
		self.assertEqual(expected, actual)
	
	def test_input_Hello_World_and_r_return_1(self):
		actual = count_letter("Hello World", "r")
		expected = 1
		self.assertEqual(expected, actual)

	def test_input_Hello_World_and_e_return_1(self):
		actual = count_letter("Hello World", "e")
		expected = 1
		self.assertEqual(expected, actual)


def count_letter(words, input):
	count = 0
	for word in words:
		if word == input:
			count += 1
	return count

unittest.main()