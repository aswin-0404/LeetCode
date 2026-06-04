class Solution(object):
    def isSameAfterReversals(self, num):
        result=""
        out=""
        for i in str(num):
            result=i+result
        result=int(result)
        for i in str(result):
            out=i+out
        if int(out)==num:
            return True
        return False


        