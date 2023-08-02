"""
Question 3
Input 1 - 5, 1, 2, 4, 3
Expected output 1 - Yes

Input 2 - 4, 1, 5, 3, 2
Expected output 2 - No

Time Complexity Achieved - O(n)
Time Complexity Reasoning - As we have one for loop this will give us O(n).
We have a while loop which again will give us O(n). Which results to O(n)
"""

import traceback


class Question3:
    """Question 3 Class"""

    perpendicular_queue = []

    def truck_queue(self, input_trucks):
        """
        Queueing Trucks for departure
        :param input_trucks:
        :return queue_possibility:
        """
        try:
            # Initializing FinalQueue
            final_queue = []

            # Finding the smallest truck for setting the starting point
            smallest_truck = int(min(input_trucks))
            current_truck = smallest_truck

            # Iterating the list to check if it is possible to queue the trucks
            for key, truck in enumerate(input_trucks):
                # Checking if current truck matches to the truck in the input list
                if truck == current_truck:
                    final_queue.append(truck)
                    current_truck += 1

                    # Checking if the perpendicular road is empty or not
                    while len(self.perpendicular_queue) != 0 and self.perpendicular_queue[-1] == current_truck:
                        final_queue.append(self.perpendicular_queue[-1])
                        self.perpendicular_queue.pop()
                        current_truck += 1

                else:
                    # Current truck does not match input truck so appending it to perpendicular road
                    self.perpendicular_queue.append(truck)

            # Returning result according to perpendicular queue size
            if len(self.perpendicular_queue) == 0:
                return "Yes"
            return "No"

        except:  # pylint: disable=bare-except
            traceback.print_exc()
            return "Error"


if __name__ == '__main__':
    input_list = [4, 1, 5, 3, 2]
    question = Question3()
    print("Input List - ", input_list)
    print("Output List - ", question.truck_queue(input_list))
