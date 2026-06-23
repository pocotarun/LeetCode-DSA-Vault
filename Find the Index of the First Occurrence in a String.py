""" 
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 """


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle)
        # return  0

# dont read only for test
sol = Solution()
haystack = "sadbutsad"
needle = "sad"
print(sol.strStr(haystack , needle))