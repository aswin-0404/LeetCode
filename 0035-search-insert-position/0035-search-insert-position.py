class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            for index,j in enumerate(nums):
                if j+1 > target:
                    return index
                elif target> nums[-1]:
                    return nums.index(nums[-1])+1
        else:
            for index,i in enumerate(nums):
                if i ==target:
                    return index