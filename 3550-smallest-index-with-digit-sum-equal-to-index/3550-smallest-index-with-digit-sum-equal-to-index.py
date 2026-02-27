class Solution(object):
    def smallestIndex(self, nums):
        out=[]
        for ind,i in enumerate(nums):
            if i <10:
                if i==ind:
                    return ind
            else:
                var=0
                for indd,j in enumerate(str(i)):
                    var+=int(j)
                if var==ind:
                    return ind
        return -1
        
        