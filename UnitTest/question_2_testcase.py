import unittest
import question_2


class Test(unittest.TestCase):
    """
    Test Cases for Question 2
    """

    question = question_2.Question2()

    def test_0(self):
        input_string = "aaa"
        expected_output = "a3"
        self.assertEqual(self.question.zip_string(input_string), expected_output)

    def test_1(self):
        input_string = "aabbbbbttttdlll"
        expected_output = "a2b5t4d1l3"
        self.assertEqual(self.question.zip_string(input_string), expected_output)

    def test_2(self):
        input_string = "aabbcccce"
        expected_output = "a2b2c4e1"
        self.assertEqual(self.question.zip_string(input_string), expected_output)

    def test_3(self):
        input_string = "a"
        expected_output = "a1"
        self.assertEqual(self.question.zip_string(input_string), expected_output)

    def test_4(self):
        input_string = "abcdefghijklmnopqrstuvwxyz"
        expected_output = "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1"
        self.assertEqual(self.question.zip_string(input_string), expected_output)

    def test_5(self):
        input_string = "111111"
        expected_output = "Wrong Format"
        self.assertEqual(self.question.zip_string(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
