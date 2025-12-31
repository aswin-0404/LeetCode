class Solution(object):
    def scoreOfString(self, s):
        lis=[]
        out=0
        for i in s:
            lis.append(ord(i))
        for j in range(1,len(lis)):
            out=out+(abs(lis[j]-lis[j-1]))
        return out

        