class Solution(object):
    def isBalanced(self, num):
        sumofeven=0
        sumofodd=0
        for ind,i in enumerate(num):
            if ind%2==0:
                sumofeven+=int(i)
            else:
                sumofodd+=int(i)
        if sumofeven == sumofodd:
            return True
        return False       