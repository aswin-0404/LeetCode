class Solution(object):
    def minimumOperations(self, nums):
        out=filter(lambda x:x%3!=0,nums)
        return len(out)