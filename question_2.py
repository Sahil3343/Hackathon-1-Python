"""
Question 2
Input 1 - aaa
Expected Output 1 - a3

Input 2 - aabbbbbttttdlll
Expected Output 2 - a2b5t4d1l3

Time Complexity Achieved - O(n)
#ime Complexity Reasoning - As a single loop is being used we
will achieve a time complexity of O(n)
"""

import traceback
from itertools import groupby


class Question2:
    """Question 2 Class"""

    def zip_string(self, input_string):
        """
        Method to Zip String
        :param input_string:
        :return result:
        """
        try:

            # Setting flag & initializing result string
            flag = True
            result = ""

            # Checking if the string only contains alphabets
            if not input_string.isalpha():
                result = "Wrong Format"
                flag = False

            # Checking if input string has length of 1 or not
            if len(input_string) == 1:
                result = input_string + "1"
                flag = False

            if flag:
                # Using groupby() to group characters and then accordingly
                # appending to result string
                for key, group in groupby(input_string):
                    temp_string = "".join(group)
                    result = result + key
                    result = result + str(len(temp_string))

            return result
        except:  # pylint: disable=bare-except
            traceback.print_exc()
            return "Error"

    def custom_logic_zip_string(self, input_string):
        """
        Custom logic for zipping string
        :param input_string:
        :return result:
        """

        # Setting flag & initializing result string
        flag = True
        result = ""

        # Checking if the string only contains alphabets
        if not input_string.isalpha():
            result = "Wrong Format"
            flag = False

        # Checking if input string has length of 1 or not
        if len(input_string) == 1:
            result = input_string + "1"
            flag = False

        # Initializing variables
        current_char = None
        char_count = 0

        if flag:
            # Iterating input string
            for key, char in enumerate(input_string):
                # Checking if this is first iteration
                if key == 0:
                    current_char = char

                # If current char is same as previous char then incrementing counter
                if current_char == char:
                    char_count += 1
                else:
                    # Appending result and changing current char and char count values
                    result += current_char + str(char_count)
                    current_char = char
                    char_count = 1

                if key == len(input_string) - 1:
                    result += current_char + str(char_count)

        return result


if __name__ == '__main__':
    input_str = "aabbbccaaa"
    question = Question2()
    print("Input String - ", input_str)
    print("Output String - ", question.custom_logic_zip_string(input_str))
