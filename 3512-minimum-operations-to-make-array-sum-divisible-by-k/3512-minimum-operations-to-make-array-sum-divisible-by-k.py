class Solution(object):
    def minOperations(self, nums, k):
        sum=0
        for i in nums:
            sum=sum+i
        if sum%k==0:
            return 0
        elif sum%k<1:
            return sum
        else:
            return int(math.ceil(sum%k))