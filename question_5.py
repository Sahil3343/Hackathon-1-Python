# Question 5
# Input -
# Expected output -

# Time Complexity Achieved -
# Time Complexity Reasoning -

import traceback


class Question5:
    def match_winner(self, matches, scores):
        try:
            # Initializing dictionary for storing team overall points & goal differences
            team_points = {}
            team_goal_differences = {}

            # Iterating through the matches and scores
            for iteration, match in enumerate(matches):

                # Getting match teams and respective scores
                team_1 = match[0]
                team_2 = match[1]

                score_1 = scores[iteration][0]
                score_2 = scores[iteration][1]

                # Finding which team has won the specific match
                # Team 1 won
                if score_1 > score_2:
                    team_points[team_1] = team_points.get(team_1, 0) + 3
                # Team 2 won
                elif score_1 < score_2:
                    team_points[team_2] = team_points.get(team_2, 0) + 3
                # Tie
                elif score_1 == score_2:
                    team_points[team_1] = team_points.get(team_1, 0) + 1
                    team_points[team_2] = team_points.get(team_2, 0) + 1

                # Adding goal differences to the dictionary
                team_goal_differences[team_1] = team_goal_differences.get(team_1, 0) + (score_1 - score_2)
                team_goal_differences[team_2] = team_goal_differences.get(team_2, 0) + (score_2 - score_1)

            # Sorting the teams according to overall points and goal differences (if any two or more teams have the same points)
            sorted_team_points = sorted(team_points.items(), key=lambda x: (x[1], team_goal_differences[x[0]], x[0]), reverse=True)
            winners = [team[0] for team in sorted_team_points[:2]]

            result = winners[0] + " " + winners[1]

            return result
        except:
            traceback.print_exc()
            return "Error"


if __name__ == '__main__':
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
        ["fcbarca", "manutd"],
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

    question = Question5()
    print("Results - ", question.match_winner(input_matches, input_scores))
