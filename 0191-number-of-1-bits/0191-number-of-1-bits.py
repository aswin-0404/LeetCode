class Solution(object):
    def hammingWeight(self, n):
        val=bin(n)
        count=0
        for i in val:
            if i =="1":
                count+=1
        return count

        