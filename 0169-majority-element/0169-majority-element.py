class Solution(object):
    def majorityElement(self, nums):
        freq={}
        out=0
        val=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for j in freq:
            if freq[j]>val:
                val=freq[j]
                out=j

        return out
        
        