# Given a string s, return the longest palindromic

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        max_length = 1
        start_index = 0
        for i in range(length-1):
            for j in range(i + 1, length):
                if max_length < j-i+1 and s[i:j + 1] == s[i:j + 1][::-1]:
                    max_length = j - i + 1
                    start_index = i
        return s[start_index:max_length + start_index]

