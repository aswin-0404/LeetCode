class Solution(object):
    def reverseOnlyLetters(self, s):
        arr=list(s)
        l=0
        r=len(s)-1
        while(l<r):
            if arr[l].isalpha() and arr[r].isalpha():
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            elif not arr[l].isalpha():
                l+=1
            elif not arr[r].isalpha():
                r-=1
        return "".join(arr)
        