# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
# The array describes the questions of an exam, where you have to process the questions in order
# (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.
# If you skip question i, you get to make the decision on the next question.
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points = [0] * n

        for i in range(n):
            current_pos = i
            total_points = 0
            for j in range(i, n):
                if current_pos == j:
                    total_points += questions[j][0]
                    brainpower = questions[j][1]
                    current_pos += brainpower + 1
            points[i] = total_points

        return max(points)