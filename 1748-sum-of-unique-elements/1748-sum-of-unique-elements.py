class Solution(object):
    def sumOfUnique(self, nums):
        arr1=[]
        arr2=[]
        out=0
        for i in nums:
            if i in arr1:
                arr2.append(i)
            else:
                arr1.append(i)
        for j in arr1:
            if j in arr2:
                arr2.append(j)
            else: 
                out+=j
        return out
        