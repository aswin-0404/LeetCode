class Solution(object):
    def gcdOfOddEvenSums(self, n):
        oddsum=0
        evensum=0
        divisor=0
        if n ==1:
            return 1
        for i in range(1,(n*2)+1):
            if i%2==0:
                evensum+=i
            else:
                oddsum+=i

        for i in range(1,oddsum//2+1):
            if oddsum %i ==0 and evensum%i ==0:
                if i>divisor:
                    divisor=i
        return divisor
        