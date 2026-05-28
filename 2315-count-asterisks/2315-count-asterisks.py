class Solution(object):
    def countAsterisks(self, s):
        if "|" in s:
            checker=None

            count=0

            for i in s:
                if i == "|":
                    if checker == None:
                        checker= False
                    else:
                        checker= not checker
                if i=="*":
                    if checker == True or checker== None:
                        count+=1
            return count
        elif "*" in s:
            return s.count("*")
        return 0
        