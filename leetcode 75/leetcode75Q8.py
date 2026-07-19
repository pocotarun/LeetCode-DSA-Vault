"""
python >> my sudo code

1. if list desanding ghate karam hai , list ki maximum 3 value same nahi ho sakti , to false return hoga
2. listindex[0] ko base manker loop chalya uske bad usse mex value nikalna fir usko bas manke uske jast baad ka max nikalna , loop kisi bhi haalt me <<< decrement me nahi chalega
3. inko me 3 bariable i < j < k me save karke campare karuga aager match hu to true return hoga loop stop
4. ye loop listindex ke aakhri se 2 index pehle hi stop hoga kyoki uske baad koi sawal hi nahi usta i < j< k ka yani last 3sre index pe stop
"""

# This class contains a method that checks if there exists an increasing triplet in a given list of
# integers.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        try:
            count = 0
            tempNums = nums
            i = j = k = None
            if len(nums) <= 2 or nums == sorted(nums, reverse=True):
                return False
            else:
                # for num in range(0, len(nums)):
                while count > len(nums) - 2:
                    tempNums = nums
                    i = tempNums[count]
                    del tempNums[count]

                for j_count in range(count, len(tempNums)):
                    if tempNums[j_count] > i:
                        j = tempNums[j_count]

                        del tempNums[tempNums.index(j)]
                        break

                for k_count in range(count, len(nums)):
                    if nums[k_count] > j:
                        k = nums[k_count]
                        break
                if (i or j or k) is None:
                    return False
                elif i < j and k < j:
                    return True

                else:
                    count += 1
        except:
            return False

# The code snippet you provided is testing the `Solution` class method `increasingTriplet` with two
# different lists `numstestlist` and `numstestlist2`. It creates an instance of the `Solution` class,
# sorts `numstestlist` in reverse order, deletes the element `3` from the list `xl`, and then prints
# the modified list `xl`.

# for testing dont read
numstestlist: list = [1, 2, 3, 4, 5]
numstestlist2: list = [5, 4, 3, 2, 1]
SolutionObj = Solution()
print(sorted(numstestlist, reverse=True))

xl = [1, 2, 3, 4, 5, 6]
del xl[xl.index(3)]
print(xl)


