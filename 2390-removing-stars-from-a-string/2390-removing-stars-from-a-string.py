class Solution(object):
    def removeStars(self, s):
        arr=[]
        for i in s:
            if i =='*':
                arr.pop()
            else:
                arr.append(i)
                
        return "".join(arr)

        