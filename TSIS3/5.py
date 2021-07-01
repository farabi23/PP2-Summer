a = list(map(int, input().split()))

d = int(input())


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

shift(a, d)
print(*a)

'''
if d < 0:
    d = abs(d)
    for i in range(d):
        a.append(a.pop(0))

else:
    for i in range(d):
        a.insert(0, a.pop())
        
print(*a)
'''    