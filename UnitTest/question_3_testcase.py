import unittest
import question_3


class Test(unittest.TestCase):
    """
    Test cases for question 3
    """

    question = question_3.Question3()

    def test_0(self):
        input_list = [5, 1, 2, 4, 3]
        expected_output = "Yes"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_1(self):
        input_list = [4, 1, 5, 3, 2]
        expected_output = "No"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_2(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = "Yes"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_3(self):
        input_list = [5, 4, 3, 2, 1]
        expected_output = "Yes"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_4(self):
        input_list = [5, 4, 3, 1, 2]
        expected_output = "Yes"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_5(self):
        input_list = [1, 2, 4, 5, 3]
        expected_output = "No"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)

    def test_6(self):
        input_list = [1, 2, 3, 6, 7]
        expected_output = "Yes"
        self.assertEqual(self.question.truck_queue(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
