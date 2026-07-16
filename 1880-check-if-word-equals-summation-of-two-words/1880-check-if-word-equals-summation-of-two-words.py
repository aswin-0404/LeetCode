class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstasci=""
        secondasci=""
        targetasci=""
        for i in firstWord:
            firstasci+=str((ord(i.lower())-ord("a")))
        for i in secondWord:
            secondasci+=str((ord(i.lower())-ord("a")))
        for i in targetWord:
            targetasci+=str((ord(i.lower())-ord("a")))

        if int(firstasci)+int(secondasci) == int(targetasci):
            return True
        return False
    