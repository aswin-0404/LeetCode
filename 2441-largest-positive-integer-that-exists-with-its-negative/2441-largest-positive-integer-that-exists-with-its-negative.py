class Solution(object):
    def findMaxK(self, nums):
        arr=[]
        for ind,i in enumerate(nums):
            if i<0:
                arr.append(nums.pop(ind))
        ele=0
        for i in arr:
            if abs(i) in nums and abs(i)>ele:
                ele=abs(i)
        if ele!=0:
            return ele
        return -1

        