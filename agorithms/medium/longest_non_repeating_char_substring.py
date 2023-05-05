# Given a string s, find the longest
# substring without repeating characters.
class Solution:
    def longestSubstring(self, s: str) -> str:
        list_str = []
        max_str = []
        start_index = 0
        root_index = 0
        while start_index < len(s):
            if s[start_index] in list_str:
                if len(list_str) > len(max_str):
                    max_str = list_str
                list_str = []
                root_index += 1
                start_index = root_index
            else:
                list_str.append(s[start_index])
                start_index += 1
        return ''.join(max_str)
