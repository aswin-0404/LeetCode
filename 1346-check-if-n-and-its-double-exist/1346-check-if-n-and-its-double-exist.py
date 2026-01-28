class Solution(object):
    def checkIfExist(self, arr):
        for ind,i in enumerate(arr):
            for jind,j in enumerate(arr):
                if ind!=jind and i*2 in arr:
                    return True
        return False


         