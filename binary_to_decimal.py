import math
n="00111"
l=len(n)
i=l-1
ls=list(n)
j=0
sum=0
while i>=0:
    sum+=sum+int(ls[j])**i
    j+=1
    i-=1
print(sum)