class Solution(object):
    def sortSentence(self, s):
        arr=s.split()
        out=sorted(arr,key=lambda x: int(x[-1]))
        s="".join(out)
        
        for i in s:
            if not i.isalpha():
                s=s.replace(i," ")
        return s.strip()