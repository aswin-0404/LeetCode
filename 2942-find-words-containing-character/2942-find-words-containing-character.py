class Solution(object):
    def findWordsContaining(self, words, x):
        arr=[]
        for ind,i in enumerate(words):
            if x in i:
                arr.append(ind)

        return arr
        