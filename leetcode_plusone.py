"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
# from typing import List


class Solution:
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        if len(str(digits[len(digits) - 1])) < 1:
            return digits
        else:
            lastDigit = [int(d) for d in str(digits[len(digits) - 1])]
            digits.pop(len(digits) - 1)
            digits.extend(lastDigit)
            return digits
            


class Solution2:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# test only >>>>>>
digits = [1, 2, 3]
digits2 = [4, 3, 2, 1]
digits3 = [9]

sol = Solution()
# print(sol.plusOne(digits))
# print(sol.plusOne(digits2))
print(sol.plusOne(digits3))
