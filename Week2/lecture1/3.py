import re

#validating phone numbers
n = int(input())

for _ in range(n):
    s = input()
    txt = re.match(r"[789]\d{9}$", s)
    if txt:
        print('YES')
    else:
        print('NO')    