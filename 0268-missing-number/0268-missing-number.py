class Solution(object):
    def missingNumber(self, nums):
        val=0
        for i in range(0,len(nums)):
            if i not in nums:
                return i
            else:
                val+=1
        if val==len(nums):
            return len(nums)
        