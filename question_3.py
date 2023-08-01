# Question 3
# Input 1 - 5, 1, 2, 4, 3
# Expected output 1 - Yes

# Input 2 - 4, 1, 5, 3, 2
# Expected output 2 - No

# Time Complexity Achieved - O(n)

import traceback


class Question3:

    def truck_queue(self, input_trucks):
        try:
            # Initializing FinalQueue & Perpendicular Road
            final_queue = []
            perpendicular_queue = []

            # Finding the smallest truck for setting the starting point
            smallest_truck = int(min(input_trucks))
            current_truck = smallest_truck

            # Iterating the list to check if it is possible to queue the trucks
            for truck in range(0, len(input_trucks)):
                # Checking if current truck matches to the truck in the input list
                if input_trucks[truck] == current_truck:
                    final_queue.append(input_trucks[truck])
                    current_truck += 1

                    # Checking if the perpendicular road is empty or not
                    while len(perpendicular_queue) != 0:
                        # Checking if the last element in the perpendicular road equals to current truck
                        if perpendicular_queue[-1] == current_truck:
                            final_queue.append(perpendicular_queue[-1])
                            perpendicular_queue.pop()
                            current_truck += 1
                        else:
                            break

                else:
                    # Current truck does not match input truck so appending it to perpendicular road
                    perpendicular_queue.append(input_trucks[truck])

            # Returning result according to perpendicular queue size
            if len(perpendicular_queue) == 0:
                return "Yes"
            else:
                return "No"

        except:
            traceback.print_exc()
            return "Error"


if __name__ == '__main__':
    input_list = [4, 1, 5, 3, 2]
    question = Question3()
    print("Input List - ", input_list)
    print("Output List - ", question.truck_queue(input_list))
