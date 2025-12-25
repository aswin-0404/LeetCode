class Solution(object):
    def reverseWords(self, s):
        n=s.split()
        new=[]
        for i in n:
            new.append(i[::-1])
        return " ".join(new)

        