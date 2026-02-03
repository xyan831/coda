# number list operations
class NumList:
    def __init__(self, lst):
        self.lst = lst
        self.lstmax = max(lst)
        self.lstmin = min(lst)
        self.avg = sum(lst)/len(lst)
        self.sd = self.get_sd()
        self.norm = self.get_norm()
    # standard deviation
    def get_sd(self):
        f = []
        for i in self.lst:
            f.append((i-self.avg)**2)
        return (sum(f)/(len(self.lst)-1))**(1/2)
    # normalize btw a and b
    def get_norm(self, a=0, b=1):
        norm = []
        for i in self.lst:
            new = (i-self.lstmin)/(self.lstmax-self.lstmin)
            norm.append((b-a)*new + a)
        return norm

if __name__ == "__main__":
    lst1 = [1, 3, 6, 3, 1]
    lstcls = NumList(lst1)
    print("list:", lstcls.lst)
    print(f"max = {lstcls.lstmax}")
    print(f"min = {lstcls.lstmin}")
    print(f"avg = {lstcls.avg}")
    print(f"standard deviation = {lstcls.sd:.2e}")
    print("normalize btw (0,1):", lstcls.norm)

