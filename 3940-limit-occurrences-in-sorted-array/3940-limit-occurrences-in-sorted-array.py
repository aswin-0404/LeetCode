class Solution(object):
    def limitOccurrences(self, nums, k):
        checker={}
        out=[]
        for  i in nums:
            if i not in checker:
                checker[i]=1
                out.append(i)
            elif i in checker and checker[i]<k:
                checker[i]+=1
                out.append(i)
        return out
        