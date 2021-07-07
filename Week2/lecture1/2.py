import re
#re.split problem

s = input()
txt = re.split(r'[,\.]+', s)
   

print("\n".join(txt))



