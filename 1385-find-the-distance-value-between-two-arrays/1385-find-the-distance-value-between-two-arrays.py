class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        validcount=0
        for i in arr1:
            count=0
            for j in arr2:
                if abs(i-j)>d:
                    count+=1
            if count==len(arr2):
                validcount+=1
        return validcount
        