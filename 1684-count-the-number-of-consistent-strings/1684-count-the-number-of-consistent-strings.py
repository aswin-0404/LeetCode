class Solution(object):
    def countConsistentStrings(self, allowed, words):
        outcount=0
        for i in words:
            count=0
            for j in i:
                if j in allowed:
                    count+=1
            if count==len(i):
                outcount+=1
        return outcount

        