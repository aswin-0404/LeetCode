class Solution(object):
    def maximumDifference(self, nums):
        out=float('-inf')
        indx=[]
        for ind,i in enumerate(nums):
            for jnd,j in enumerate(nums):
                if i<j and jnd not in indx:
                    out=max(out,(j-i))
            indx.append(ind) 
        if out == float('-inf'):
            return -1
        return out
        
        