def alternate_subarray(a,n):
    l=0
    r=1
    c=0
    t=0;
    while(r<n):
        if((a[l]<0 and a[r]<0) or(a[l]>0 and a[r]>0)):
            c=0
        if((a[l]>0 and a[r]<0) or (a[l]<0 and a[r]>0)):
            c+=1
            t=max(t,c)
        l+=1
        r+=1
    return t+1


n=int(input())
a=list(map(int,input().split()))
t=alternate_subarray(a,n)
print(t)
