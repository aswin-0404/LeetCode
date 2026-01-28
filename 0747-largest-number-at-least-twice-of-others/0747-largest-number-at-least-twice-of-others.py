class Solution(object):
    def dominantIndex(self, nums):
        arr=sorted(nums)
        largest=arr[-1]
        count=0
        for i in arr:
            if i !=largest:
                if i*2<=largest:
                    count+=1
        if count==len(nums)-1:
            return nums.index(largest)
        else:
            return -1

        
        