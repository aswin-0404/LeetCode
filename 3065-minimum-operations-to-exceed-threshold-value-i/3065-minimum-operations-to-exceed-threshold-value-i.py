class Solution(object):
    def minOperations(self, nums, k):
        arr=sorted(nums)
        count=0
        for i in arr:
            if i <k:
                count+=1
            else:
                break
        return count