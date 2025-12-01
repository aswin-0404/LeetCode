class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr=len(nums)
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums