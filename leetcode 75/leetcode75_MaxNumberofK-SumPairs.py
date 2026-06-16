class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        pairs = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                pairs += 1
            elif (total := nums[left] + nums[right]) > k:
                right -= 1
            elif total < k:
                left +=1   
        return pairs        


    # index = 0
    # for i in range(0, len(nums)):
    #     while len(nums) != 0:
    #         if nums[i] + nums[index] == k:
    #             nums.pop(i)
    #             nums.pop(index)

    #             continue
    #         else:
    #          index+=1
    # pair = 0
    # numsn = nums.sort()
    # for i in range(0, len(numsn)):
    #     if numsn[i] + numsn[len(numsn) - 1 - i] == k:
    #         i += 1
    #         pair += 1
    #         continue
    #     else:
    #         return pair


# Ab yahan tum azaad ho!
# Agar dono ka total == k hai, toh dono ko ek-ek kadam andar lao.
# Agar total k se bada hai, toh sirf 'right' wale ko peeche lao (right -= 1).
# Agar total k se chhota hai, toh sirf 'left' wale ko aage badhao (left += 1).


# >> test phase
sol = Solution()
nums = [1, 2, 3, 4, 5]

print(sol.maxOperations(nums, 4))
# >> samagri
# remove karne ke liye .pop() ka use karega
