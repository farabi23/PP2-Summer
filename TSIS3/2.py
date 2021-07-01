a = input().split()

mlist = []

maxi = 1000

for i in range(len(a)):
    if int(a[i]) > 0 and int(a[i]) < maxi:
        maxi = int(a[i])

print(maxi)