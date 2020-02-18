n=int(input("enter the decimal number"))
l=[]
a=n
ls=[]
while(n!=0):
    l.append(n%2)
    n=n//2
m=len(l)-1
while m!=-1:
    ls.append(l[m])
    m=m-1
c=0
for i in range(len(ls)):
    if ls[i]==1:
        c+=1
print(ls)
print(c)
