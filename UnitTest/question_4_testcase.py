import unittest
import question_4

class Testing(unittest.TestCase):
    """
    Test cases for Question 4
    """

    question = question_4.Question4()

    def test_0(self):
        input_list = ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk"]
        input_right_hand = ['j', 'k']
        input_left_hand = ['d', 'f']
        expected_output = 6.1
        self.assertEqual(self.question.typing_time(input_list, input_right_hand), expected_output)

    def test_1(self):
        input_list = ["a", "b", "c", "d", "e", "f"]
        input_right_hand = ['a', 'b', 'c']
        input_left_hand = ['d', 'e', 'f']
        expected_output = 1.2
        self.assertEqual(self.question.typing_time(input_list, input_right_hand), expected_output)

    def test_2(self):
        input_list = []
        input_right_hand = []
        input_left_hand = []
        expected_output = 0
        self.assertEqual(self.question.typing_time(input_list, input_right_hand), expected_output)

    def test_3(self):
        input_list = ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk", "fdjkd"]
        input_right_hand = ['j', 'k']
        input_left_hand = ['d', 'f']
        expected_output = 6.45
        self.assertEqual(self.question.typing_time(input_list, input_right_hand), expected_output)

    def test_4(self):
        input_list = ["abcdef", "bcdefa", "ccddee", "aaaaa", "deacb"]
        input_right_hand = ['a', 'b', 'c']
        input_left_hand = ['d', 'e', 'f']
        expected_output = 9.2
        self.assertEqual(self.question.typing_time(input_list, input_right_hand), expected_output)


if __name__ == '__main__':
    unittest.main()
