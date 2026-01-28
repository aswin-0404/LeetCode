class Solution(object):
    def checkIfExist(self, arr):
        count=0
        for ind,i in enumerate(arr):
            if i*2 in arr:
                if ind != arr.index(i*2):
                    count+=1
        if count>0:
            return True
        else:
            return False