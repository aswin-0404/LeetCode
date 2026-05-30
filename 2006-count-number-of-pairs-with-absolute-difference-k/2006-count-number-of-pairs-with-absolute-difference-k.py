class Solution(object):
    def countKDifference(self, nums, k):
        count=0

        for ind,i in enumerate(nums):
            for jnd,j in enumerate(nums):
                if ind != jnd and abs(i-j) == k:
                    count+=1
        if count >0:
            return count//2
        return 0