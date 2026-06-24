class Solution(object):
    def digitFrequencyScore(self, n):
        freq={}
        out=0
        for i in str(n):
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i,j in freq.items():
            out+=(j*int(i))
        return out
        