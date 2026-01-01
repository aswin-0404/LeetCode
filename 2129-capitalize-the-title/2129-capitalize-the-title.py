class Solution(object):
    def capitalizeTitle(self, title):
        arr=title.split()
        out=[]
        for i in arr:
            if len(i)>2:
                out.append(i.capitalize())
            elif len(i)==2:
                out.append(i.lower())
            else:
                out.append(i.lower())
        return " ".join(out)

