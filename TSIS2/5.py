class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mylist = []
        mult = 1
        sum = 0
        n = str(n)
        for i in range(len(n)):
            mylist.append(n[i])
            
        for j in range(len(mylist)):
            mult = mult * int(mylist[j])
            sum = sum + int(mylist[j])
            
        return mult - sum