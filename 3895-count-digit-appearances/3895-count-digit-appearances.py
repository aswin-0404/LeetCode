class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count=0

        for i in nums:
            for j in str(i):
                if int(j) == digit:
                    count+=1
        return count