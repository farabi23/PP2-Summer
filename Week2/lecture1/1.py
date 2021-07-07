import re
#Floating number problem

s = int(input())
for _ in range(s):
    txt = input()
    x = re.match(r"^[-+]?[0-9]*\.[0-9]+$", txt)
    print(bool(x))
   