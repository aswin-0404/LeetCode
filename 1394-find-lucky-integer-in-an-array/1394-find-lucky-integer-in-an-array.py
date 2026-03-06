class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        l=0

        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            
        for i in freq:
            if freq[i]==i and freq[i]>l:
                l=freq[i]
        if l!=0:
            return l
        return -1