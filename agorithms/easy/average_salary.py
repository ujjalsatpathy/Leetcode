# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10-5 of the actual answer will be accepted.
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sortd_salary = sorted(salary)
        total = sum(sortd_salary[1:len(sortd_salary) - 1])/(len(sortd_salary)-2)
        return total
