class Solution(object):
    def searchRange(self, nums, target):
        out=[]
        f=None
        l=None
        for ind,i in enumerate(nums):
            if i==target:
                if f==None:
                    f=ind
                    l=ind
                elif ind>l:
                    l=ind
        if f!= None and l != None:
            out.append(f)
            out.append(l)
            return out
        else:
            return [-1,-1]
                





        