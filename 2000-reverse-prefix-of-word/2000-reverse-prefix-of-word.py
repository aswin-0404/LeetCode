class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        else:
            arr=list(word)
            left=0
            right=arr.index(ch)

            while(left<right):
                arr[right], arr[left]=arr[left] ,arr[right]
                left+=1
                right-=1
                
            return "".join(arr)

        