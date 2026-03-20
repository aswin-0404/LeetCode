class Solution(object):
    def findPermutationDifference(self, s, t):
        sum=0
        for ind,i in enumerate(s):
            for jind,j in enumerate(t):
                if i==j:
                    sum+=abs(ind-jind)
        return sum
        