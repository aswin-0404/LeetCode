class Solution(object):
    def findDuplicates(self, nums):
        arr=set()
        dup=set()
        for i in nums:
            if i not in arr:
                arr.add(i)
            else:
                dup.add(i)
        return list(dup)
        