class Solution(object):
    def sumOfMultiples(self, n):
        sum=0
        for i in range(0,n+1):
            if i%3==0:
                sum+=i
                continue
            elif i%5==0:
                sum+=i
                continue
            elif i%7==0:
                sum+=i
                continue
        return sum

        