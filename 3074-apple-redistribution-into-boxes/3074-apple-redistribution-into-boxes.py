class Solution(object):
    def minimumBoxes(self, apple, capacity):
        count=reduce(lambda x,y:x+y,apple)
        capacity.sort(reverse=True)
        cap=0
        num=1
        for i in capacity:
            cap=cap+i
            if cap>=count:
                return num
            else:
                num+=1
        return num

        