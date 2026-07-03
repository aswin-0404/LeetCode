class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0

        digit = str(digit)

        for i in nums:
            for j in str(i):
                if j == digit:
                    count+=1
        return count