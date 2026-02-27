class Solution(object):
    def kthDistinct(self, arr, k):
        uni=[]
        dup=[]
        out=[]
        for i in arr:
            if i not in uni:
                uni.append(i)
            else:
                dup.append(i)
        for i in uni:
            if i not in dup:
                out.append(i)
        if len(out)<k:
            return ""
        else:
            return out[k-1]

        