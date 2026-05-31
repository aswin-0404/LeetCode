class Solution(object):
    def findMaxAverage(self, nums, k):
        total=0
        maxval=float('-inf')


        l=0
        for r in range(len(nums)):
            total+=nums[r]
        
            if abs((r+1)-l)==k:
                maxval=max(total , maxval)
                total-=nums[l]
                l+=1
        return maxval/float(k)
        