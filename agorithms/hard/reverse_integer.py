# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:

        numb = str(abs(x))
        if x < 0:
            reversed_number = -int(numb[::-1])
        else:
            reversed_number = int(numb[::-1])

        if reversed_number >= 2 ** 31 - 1 or reversed_number <= -2 ** 31:
            return 0
