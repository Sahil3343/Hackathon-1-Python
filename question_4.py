"""
Question 4
Input - ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk"]
Expected output - 6.1 seconds

Time Complexity Achieved - O(n * m)
Time Complexity Reasoning - n is the number of words and m is the number of characters in the word
"""

import traceback


class Question4:
    """Question 4 Class"""

    RIGHT_HAND = "RIGHT"
    LEFT_HAND = "LEFT"
    FIRST_CHAR_TIME = 0.2
    SAME_HAND_TIME = 0.4
    DIFFERENT_HAND_TIME = 0.2

    def typing_time(self, input_words, input_righthand):
        """
        Finding time taken to type a word
        :param input_words:
        :param input_righthand:
        :param input_lefthand:
        :return total_time_taken:
        """
        try:
            # Initializing variables
            total_time_taken = 0
            word_time = {}
            previous_hand = None

            # Iterating input word list
            for key, word in enumerate(input_words):
                time = 0

                # Checking if the word has already been typed previously or not
                if word in word_time:
                    # Taking the half-time of what was previously typed
                    time = float(word_time.get(word)) / 2.0
                    word_time[word] = time
                    total_time_taken += time
                else:
                    time = self.FIRST_CHAR_TIME

                    # Checking first char hand
                    if word[0] in input_righthand:
                        previous_hand = self.RIGHT_HAND
                    else:
                        previous_hand = self.LEFT_HAND

                    for char in word[1:]:
                        # Checking in char is part of right hand or not
                        if char in input_righthand:
                            # Checking if previous char and current char are same hand (right)
                            if previous_hand == self.RIGHT_HAND:
                                time += self.SAME_HAND_TIME
                            else:
                                time += self.DIFFERENT_HAND_TIME
                                previous_hand = self.RIGHT_HAND
                        else:
                            # Checking if previous char and current char are same hand (left)
                            if previous_hand == self.LEFT_HAND:
                                time += self.SAME_HAND_TIME
                            else:
                                time += self.DIFFERENT_HAND_TIME
                                previous_hand = self.LEFT_HAND

                    # Appending word and time taken to dictionary
                    word_time[word] = time
                    # Updating total time taken
                    total_time_taken += time

            return round(total_time_taken, 2)
        except:  # pylint: disable=bare-except
            traceback.print_exc()
            return -1


if __name__ == '__main__':
    input_list = ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk"]
    input_right = ['j', 'k']
    input_left = ['d', 'f']
    question = Question4()
    print("Input Words - ", input_list)
    print("Output Time Taken - ", question.typing_time(input_list, input_right))
