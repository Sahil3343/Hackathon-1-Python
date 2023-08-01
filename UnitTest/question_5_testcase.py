import unittest
import question_5

class Testing(unittest.TestCase):
    """
    Test cases for Question 5
    """

    question = question_5.Question5()

    def test_0(self):
        input_matches = [
        ["manutd", "arsenal"],
        ["lyon", "manutd"],
        ["fcbarca", "lyon"],
        ["fcbarca", "arsenal"],
        ["manutd", "fcbarca"],
        ["arsenal", "lyon"],
        ["arsenal", "manutd"],
        ["manutd", "lyon"],
        ["arsenal", "fcbarca"],
        ["lyon", "fcbarca"],
        ["lyon", "arsenal"],
        ["fcbarca", "manutd"]
    ]

        input_scores = [
        [8, 2],
        [1, 2],
        [0, 0],
        [5, 1],
        [3, 1],
        [6, 0],
        [0, 0],
        [4, 2],
        [2, 2],
        [0, 3],
        [1, 0],
        [0, 1],
    ]

        expected_output = "manutd fcbarca"
        self.assertEqual(self.question.match_winner(input_matches, input_scores), expected_output)

    def test_1(self):
        input_matches = [
        ["a", "b"],
        ["a", "c"],
        ["a", "d"],
        ["b", "a"],
        ["b", "c"],
        ["b", "d"],
        ["c", "a"],
        ["c", "b"],
        ["c", "d"],
        ["d", "a"],
        ["d", "b"],
        ["d", "c"]
    ]

        input_scores = [
        [3, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [4, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [1, 0],
        [3, 0],
        [0, 0],
        [0, 0],
    ]

        expected_output = "d b"
        self.assertEqual(self.question.match_winner(input_matches, input_scores), expected_output)


if __name__ == '__main__':
    unittest.main()