class Solution(object):
    def findMaxAverage(self, nums, k):
        total=0
        avg=float('-inf')

        l=0
        for r in range(len(nums)):
            total+=nums[r]
        
            if abs((r+1)-l)==k:
                avg=max(total/float(k) , avg)
                total-=nums[l]
                l+=1
        return avg
        