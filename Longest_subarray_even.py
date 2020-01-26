n=int(input())
c=0
t=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if(a[i]%2==0):
        c+=1
    else:
        t=max(t,c)
        c=0
print(t)
