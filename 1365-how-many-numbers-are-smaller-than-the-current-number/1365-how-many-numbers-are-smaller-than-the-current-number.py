class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        liss=[]
        count=0
        for i in nums:
            for j in nums:
                if i>j:
                    count+=1
            liss.append(count) 
            count=0
        return liss  