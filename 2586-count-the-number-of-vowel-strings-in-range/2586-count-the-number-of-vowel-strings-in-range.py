class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels="aeiou"
        count=0
        for i in range(left,right+1):
            # if words[i][0] in vowels and words[i][len(words[i])-1] in vowels:
            #     count+=1
            incount=0
            for j in vowels:
                
                first=words[i][0]
                last=words[i][len(words[i])-1]
                if j == first:
                    incount+=1
                if j ==last:
                    incount+=1
            if incount ==2:
                count+=1
        return count

        