class Solution(object):
    def isGood(self, nums):
        freq={}

        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        sort_freq=sorted(freq.items(),key=lambda x : x[0])
        count=0
        count2=0
        for x,y in sort_freq:
            if x > len(nums)-1:
                return False
    
            elif x == len(nums)-1 and y ==2:
                count+=1
    
            elif x < len(nums)-1 and y ==1:
                count2+=1

        if count ==1 and count2 == len(nums)-2:
            return True
        else:
            return False
                
            
       

        