import unittest
import question_6


class Testing(unittest.TestCase):
    """
    Test cases for Question 6
    """

    question = question_6.Question6()

    def test_0(self):
        input_string = "123"
        expected_output = 3
        self.assertEqual(self.question.total_possible_decodes(input_string), expected_output)

    def test_1(self):
        input_string = "1"
        expected_output = 1
        self.assertEqual(self.question.total_possible_decodes(input_string), expected_output)

    def test_2(self):
        input_string = ""
        expected_output = 0
        self.assertEqual(self.question.total_possible_decodes(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
