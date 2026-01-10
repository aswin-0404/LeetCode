class Solution(object):
    def reversePrefix(self, s, k):
        arr=list(s)
        newarr=arr[:k]
        arr=arr[k:]
        arr=newarr[::-1]+arr

        return "".join(arr)
        