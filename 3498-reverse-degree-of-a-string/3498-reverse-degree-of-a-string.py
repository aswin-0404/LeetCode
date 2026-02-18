class Solution(object):
    def reverseDegree(self, s):
        sum=0
        for ind,i in enumerate(s):
            sum+=(ind+1)*(27-(ord(i)-96))  
        return sum


        