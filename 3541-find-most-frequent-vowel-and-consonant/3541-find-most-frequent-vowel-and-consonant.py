class Solution(object):
    def maxFreqSum(self, s):
        mylist=["a","e","i","o","u"]
        freq={}
        vowmax=0
        conmax=0
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if i in mylist and freq[i]>vowmax:
                vowmax=freq[i]
            elif i not in mylist and freq[i]>conmax:
                conmax=freq[i]
            
        return conmax+vowmax
                