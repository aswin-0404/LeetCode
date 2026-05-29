class Solution(object):
    def minElement(self, nums):
        out=[]

        for i in nums:
            sum=0
            for j in  str(i):
                sum+=int(j)
            out.append(sum)
        out.sort()
        return out[0]
        
        
        