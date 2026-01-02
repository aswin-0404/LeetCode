class Solution(object):
    def repeatedNTimes(self, nums):
        arr=[]
        arr1=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                arr1.append(i)
        return arr1[0]
        