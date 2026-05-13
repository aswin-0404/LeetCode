class Solution(object):
    def sortSentence(self, s):
        arr=s.split()
        out=sorted(arr,key=lambda x: int(x[-1]))
        new="".join(out)
        
        for ind,i in enumerate(new):
            if not i.isalpha():
                new=new.replace(i," ")
        return new.strip()