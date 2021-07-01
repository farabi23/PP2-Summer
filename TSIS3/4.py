b = input().split()
d = 0
for i in range(len(b)):
    j = i - d
    if b[j] == '0':
        b.append(b.pop(j))
        d += 1
print(*b)
