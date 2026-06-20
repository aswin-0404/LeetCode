class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        l=0

        checker=0

        while(l<=len(s)-2):
            if abs(int(s[l])-int(s[l+1])) <=2:
                checker+=1
            l+=1
        if checker == len(s)-1:
            return True

        return False
        
        