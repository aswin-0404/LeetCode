class Solution(object):
    def shuffle(self, nums, n):
        k=n
        lis=[]
        for i in range(0,n):
            lis.append(nums[i])
            for j in range(k,len(nums)):
                lis.append(nums[j])
                k+=1
                break
        return lis
            
        