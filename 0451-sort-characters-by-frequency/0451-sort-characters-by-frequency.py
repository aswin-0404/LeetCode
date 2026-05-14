class Solution(object):
    def frequencySort(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1

        out=""
        new=sorted(freq.items(),key=lambda x : x[1],reverse=True)
        
        for i,j in new:
            out+=i*j
            
        return out
        