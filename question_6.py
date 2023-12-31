"""
Question 6
Input - 123
Expected output - 3

Time Complexity Achieved - O(n)
Time Complexity Reasoning - As we are looping the complete message once
it will have a time complexity of O(n)
"""

import traceback


class Question6:
    """Question 6 Class"""
    def total_possible_decodes(self, message):
        """
        Finding total possibilities to decode a message
        :param message:
        :return decode_possibilities:
        """
        try:

            # Setting flag & initializing result
            flag = True
            result = None

            # Checking if the length of the input message is 0 or not
            if len(message) == 0:
                result = 0
                flag = False

            if flag:
                # Initializing count list and setting default values
                count = [0] * (len(message) + 1)
                count[0] = 1

                # Checking if the first digit is 0 or not
                if message[0] == 0:
                    count[1] = 0
                else:
                    count[1] = 1

                # Iterating string to look at possibilities of decoding
                for i in range(2, len(message) + 1):
                    # Checking for single digits. If it is between 1 and 9 (inclusive)
                    single_digit = int(message[i - 1])
                    if 1 <= single_digit <= 9:
                        count[i] += count[i - 1]

                    # Checking for two digits. If it is between 10 and 26 (inclusive)
                    two_digit = int(message[i - 2:i])
                    if 10 <= two_digit <= 26:
                        count[i] += count[i - 2]

                result = count[len(message)]

            return result
        except:  # pylint: disable=bare-except
            traceback.print_exc()
            return -1


if __name__ == '__main__':
    input_string = "123"
    question = Question6()
    print("Input String - ", input_string)
    print("Output - ", question.total_possible_decodes(input_string))
