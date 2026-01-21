class Solution(object):
    def createTargetArray(self, nums, index):
        arr=[]
        for i in range(len(nums)) :
            val=nums[i]
            arr.insert(index[i],val)
        return arr
            
        