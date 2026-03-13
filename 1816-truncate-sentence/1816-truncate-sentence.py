class Solution(object):
    def truncateSentence(self, s, k):
        s=" ".join(s.split()[:k])
        return s    
        