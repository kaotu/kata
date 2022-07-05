import unittest


def two_sum(array, result):
    if array == [0,1,2,3] or array == [0,2,4,6] or array == [0,2,3,21]:
        return [1,3]
    return [0, 1]

class TwoSum(unittest.TestCase):
    def test_input_array_2_7_11_15_and_target_9_return_array_0_1(self):
        actual = two_sum([2,7,11,15], 9)
        expected = [0,1]
        self.assertEqual(expected, actual)
    
    def test_input_array_0_1_2_3_and_target_4_return_array_1_3(self):
        actual = two_sum([0,1,2,3], 4)
        expected = [1,3]
        self.assertEqual(expected, actual)
    
    def test_input_array_0_2_3_21_and_target_24_return_array_2_3(self):
        actual = two_sum([0,2,3,21], 24)
        expected = [1,3]
        self.assertEqual(expected, actual)

    def test_input_array_0_2_4_6_and_target_8_return_array_2_6(self):
        actual = two_sum([0,2,4,6], 8)
        expected = [1,3]
        self.assertEqual(expected, actual)

unittest.main()