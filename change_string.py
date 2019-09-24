def change(s1,s2):
    ls=list()
    ls1=list()
    d=dict()
    d1=dict()
    ls=list(s1)
    ls1=list(s2)
    ls.sort()
    ls1.sort()
    n=len(ls)
    m=len(ls1)
    cnt=0
    print(ls)
    print(ls1)
    if len(ls)!=len(ls1):
        return -1
    if ls == ls1:
        return(1)
    else:
        return(-1)
if __name__ == "__main__": 
        s1='bcefd'
        s2='adfeb'
        print(change(s1,s2))
        