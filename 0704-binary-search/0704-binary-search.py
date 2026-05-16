class Solution(object):
    def search(self, nums, target):
        l=0
        r=len(nums)-1
        

        if target not in nums:
            return -1
        else:
            while(l<=r):
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
        
        