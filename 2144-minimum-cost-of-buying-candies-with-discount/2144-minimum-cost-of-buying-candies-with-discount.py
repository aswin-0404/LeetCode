class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total=cost[0]
        if len(cost)>2:
            for i in range(1,len(cost)):
                if (i+1)%3!=0:
                    total+=cost[i]
        else:
            for i in range(1,len(cost)):
                total+=cost[i]
    
        return total