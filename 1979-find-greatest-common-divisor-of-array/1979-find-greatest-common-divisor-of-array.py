class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s=nums[0]
        l=nums[len(nums)-1]
        num=0
        for i in range(1,min(s,l)+1):
            if s%i==0 and l%i==0:
                num=i

        return num