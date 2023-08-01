# Question 2
# Input 1 - aaa
# Expected Output 1 - a3

# Input 2 - aabbbbbttttdlll
# Expected Output 2 - a2b5t4d1l3

# Time Complexity Achieved - O(n)

import traceback
from itertools import groupby


class Question2:
    """Question 2 Class"""
    def zip_string(self, input_string):
        try:
            # Checking if the string only contains alphabets
            if not input_string.isalpha():
                return "Wrong Format"

            # Checking if input string has length of 1 or not
            if len(input_string) == 1:
                return input_string + "1"

            # Initializing result string
            result = ""

            # Using groupby() to group characters and then accordingly appending to result string
            for key, group in groupby(input_string):
                temp_string = "".join(group)
                result = result + key
                result = result + str(len(temp_string))

            return result
        except:
            traceback.print_exc()
            return "Error"


if __name__ == '__main__':
    input_string = "aabbbccaaa"
    question = Question2()
    print("Input String - ", input_string)
    print("Output String - ", question.zip_string(input_string))
