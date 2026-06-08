nums = [0,1,0,3,12]
def moveZeroes(self, nums):
    count = nums.count(0)
    while 0 in nums :
        nums.remove(0)


    for count in range(count):
        nums.append(0)
    return nums


print(moveZeroes(nums))