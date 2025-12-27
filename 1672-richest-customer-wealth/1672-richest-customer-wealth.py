class Solution(object):
    def maximumWealth(self, accounts):
        sum=0
        val=0
        for i in accounts:
            val=reduce(lambda x,y:x+y,i)
            if val>sum:
                sum=val

        return sum

        