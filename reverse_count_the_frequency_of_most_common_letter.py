def reverse(string):
    ls=list(string)
    l=list()
    d=dict()
    n=len(ls)-1
    while n>=0:
        l.append(ls[n])
        n-=1
    st=""
    print(st.join(l))
    ll=list(st)
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    lss=list()
    for k,v in d.items():
        lss.append((v,k))
    lss.sort(reverse=True)
    lsss=list(lss[0])
    print(lsss[1])
if __name__ == "__main__":
    input = 'geeksforgeeks'
    reverse(input) 