# Question 4
# Input - ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk"]
# Expected output - 6.1 seconds

# Time Complexity Achieved - O(n * m)
# Time Complexity Reasoning - n is the number of words and m is the number of characters in the word

import traceback

class Question4:
    def typing_time(self, input_words, input_righthand, input_lefthand):
        try:
            # Initializing variables
            total_time_taken = 0
            word_time = {}
            previous_hand = None

            # Iterating input word list
            for key, word in enumerate(input_words):
                temp_time = 0

                # Checking if the word has already been typed previously or not
                if word in word_time.keys():
                    # Taking the half time of what was previously typed
                    time = float(word_time.get(word)) / 2.0
                    word_time[word] = time
                    total_time_taken += time
                else:
                    # Iterating word for char
                    for iteration, char in enumerate(word):
                        # First character of the word
                        if iteration == 0:
                            temp_time += 0.2
                            # Setting hand typed with
                            if char in input_righthand:
                                previous_hand = "RIGHT"
                            else:
                                previous_hand = "LEFT"
                        else:
                            if char in input_righthand:
                                # If previous hand (right) matches with current hand (right)
                                if previous_hand == "RIGHT":
                                    temp_time += 0.4
                                # If previous hand (left) doesn't match with current hand (right)
                                else:
                                    temp_time += 0.2
                                    previous_hand = "RIGHT"
                            else:
                                # If previous hand (left) matche with current hand (left)
                                if previous_hand == "LEFT":
                                    temp_time += 0.4
                                # If previous hand (right) doesn't match with current hand (left)
                                else:
                                    temp_time += 0.2
                                    previous_hand = "LEFT"

                    # Appending word and time taken to dictionary
                    word_time[word] = temp_time
                    # Updating total time taken
                    total_time_taken += temp_time

            return total_time_taken
        except:
            traceback.print_exc()
            return -1


if __name__ == '__main__':
    input_list = ["fdjkd", "dfjdk", "dfd", "fdjkd", "kkjjk"]
    input_right = ['j', 'k']
    input_left = ['d', 'f']
    question = Question4()
    print("Input Words - ", input_list)
    print("Output Time Taken - ", question.typing_time(input_list, input_right, input_left))
