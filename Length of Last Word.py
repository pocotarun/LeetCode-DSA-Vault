"""

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.



Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = len(s)
        s = s.strip()
        if len(s) == 0:
            return 0
        if(s.find(" ") != -1):
            return len(s) - 1 - s.rindex(" ")
        else:
            return len(s)


# dont read only for test
s = "Hello World"
s2 = "luffy is still joyboy"
s2_ = "a"
s3 = "   fly me   to   the moon  "
sol = Solution()
print(sol.lengthOfLastWord(s2_))
