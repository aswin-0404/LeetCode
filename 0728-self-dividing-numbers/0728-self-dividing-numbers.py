class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr=[]
        for  i in range(left,right+1):
            if i<10:
                arr.append(i)
            else:
                val=str(i)
                l=len(val)
                count=0
                if '0' not in val:
                    for j in range(l):
                        if i%int(val[j])==0:
                            count+=1
                        if count==l:
                            arr.append(i)
        return arr