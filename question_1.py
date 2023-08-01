# Question 1
# Input - 1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0
# Expected Output - 1, 2, -4, -1, -1, 1, 3, 7, 5, 0, 0, 0, 0, 0

# Time Complexity Achieved - O(n)
# Time Complexity Reasoning - As we have two for loops (not nested) we will achieve a time complexity of O(n)

import traceback


class Question1:
    """Question 1 Class"""
    def rearranging_list(self, input_list):
        """Rearranging list"""
        try:
            # Initializing the result list
            result = []

            # First Loop - Appending all non-zero numbers to the result list
            for number in input_list:
                if number != 0:
                    result.append(number)

            # Second Loop - Appending all zero numbers to the result list
            for number in input_list:
                if number == 0:
                    result.append(number)

            # Returning result list
            return result
        except:  # pylint: disable=bare-except
            traceback.print_exc()
            return "Error"


if __name__ == '__main__':
    in_list = [1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0]
    question = Question1()
    print("Input List - ", in_list)
    print("Output List - ", question.rearranging_list(input_list=in_list))
