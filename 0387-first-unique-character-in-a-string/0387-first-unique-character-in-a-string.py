class Solution(object):
    def firstUniqChar(self, s):
        u=[]
        d=[]
        out=""
        for i in s:
            if i not in u:
                u.append(i)
            else:
                d.append(i)
        w=set(d)
        for i in u:
            if i not in w:
                out=out+i
        if len(out)>0:
            return s.index(out[0])
        else:
            return -1