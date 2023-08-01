import unittest
import question_1


class Test(unittest.TestCase):
    """
    Test Case for Question 1
    """

    question = question_1.Question1()

    def test_0(self):
        input_list = [1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0]
        expected_output = [1, 2, -4, -1, 3, 7, 5, 1, -1, 0, 0, 0, 0, 0]
        self.assertEqual(self.question.rearranging_list(input_list), expected_output)

    def test_1(self):
        input_list = [0, 0, 0, 1, 8, 4, 0, 32, 8, 0, 3, 7]
        expected_output = [1, 8, 4, 32, 8, 3, 7, 0, 0, 0, 0, 0]
        self.assertEqual(self.question.rearranging_list(input_list), expected_output)

    def test_2(self):
        input_list = []
        expected_output = []
        self.assertEqual(self.question.rearranging_list(input_list), expected_output)

    def test_3(self):
        input_list = [10]
        expected_output = [10]
        self.assertEqual(self.question.rearranging_list(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
