class Solution(object):
    def leftRightDifference(self, nums):
        out=[]
        for i in range(len(nums)):
            if i ==0:
                out.append(abs(0-sum(nums[i+1:len(nums)])))
            elif i ==len(nums)-1:
                out.append(abs(sum(nums[0:len(nums)-1])-0))
            else:
                out.append(abs(sum(nums[0:i])-sum(nums[i+1:len(nums)])))
        return out