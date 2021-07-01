a = input().split()
mlist = []
for i in range(len(a)):
    
    if int(i) % 2 == 0:
        mlist.append(int(a[i]))
print(*mlist)        
        
