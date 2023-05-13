# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
# The array describes the questions of an exam, where you have to process the questions in order
# (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.
# If you skip question i, you get to make the decision on the next question.
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        for i in range(n):
            points, brainpower = questions[i]

            # Calculate the maximum points that can be earned by skipping the current question
            skip_points = dp[i - 1] if i > 0 else 0

            # Calculate the maximum points that can be earned by solving the current question
            solve_points = 0
            if i >= brainpower:
                solve_points = dp[i - brainpower] + points

            # Choose the maximum of skip_points and solve_points
            dp[i] = max(skip_points, solve_points)

        return dp[n - 1]


cls = Solution()
print(cls.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))
