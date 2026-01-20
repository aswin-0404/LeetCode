class Solution(object):
    def containsDuplicate(self, nums):
        n=set(nums)
        if len(n)!=len(nums):
            return True
        else:
            return False
        