class Solution(object):
    def minElement(self, nums):
        out=None

        for i in nums:
            sum=0
            for j in  str(i):
                sum+=int(j)
            if sum < out or out ==None:
                out=sum
        
        return out
        
        
        