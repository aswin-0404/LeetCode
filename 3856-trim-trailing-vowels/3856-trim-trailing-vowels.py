class Solution(object):
    def trimTrailingVowels(self, s):
        indx=None
        count=0
        for ind,i  in enumerate(reversed(s)):
            if i not in "aeiou" and ind == 0:
                return s
            elif i not in "aeiou":
                indx=ind
                return s[0:(len(s)-indx)] 
            elif i in "aeiou":
                count+=1
        if count == len(s):
            return ""