class Solution(object):
    def mirrorDistance(self, n):
        val=""
        for i in str(n):
            val=i+val
        return abs(n-int(val))
        