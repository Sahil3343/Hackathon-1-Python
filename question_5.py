"""
Question 5
Input -
Expected output -

Time Complexity Achieved - O(n + m)
Time Complexity Reasoning - As we have 2 loops. One iterates n matches
and other iterates m teams
"""
import heapq
import traceback


class Question5:
    """Question 5 Class"""

    def match_winner(self, matches, scores):
        """
        Find the first and second place of the series
        :param matches:
        :param scores:
        :return winner:
        """
        try:
            # Initializing dictionary for storing team overall points, goal differences, top teams
            team_points = {}
            team_goal_differences = {}
            top_teams = []

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
                    team_points[team_2] = team_points.get(team_2, 0) + 0
                # Team 2 won
                elif score_1 < score_2:
                    team_points[team_2] = team_points.get(team_2, 0) + 3
                    team_points[team_1] = team_points.get(team_1, 0) + 0
                # Tie
                elif score_1 == score_2:
                    team_points[team_1] = team_points.get(team_1, 0) + 1
                    team_points[team_2] = team_points.get(team_2, 0) + 1

                # Adding goal differences to the dictionary
                team_goal_differences[team_1] = team_goal_differences.get(team_1, 0) + (score_1 - score_2)
                team_goal_differences[team_2] = team_goal_differences.get(team_2, 0) + (score_2 - score_1)

            # Iterating the team points dictionary
            for team, points in team_points.items():
                # Pushing related scores into top_teams
                heapq.heappush(top_teams, (-points, -team_goal_differences[team], team))

            result = heapq.heappop(top_teams)[2] + " " + heapq.heappop(top_teams)[2]

            return result
        except:  # pylint: disable=bare-except
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
