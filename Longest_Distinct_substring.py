str=input()
s=set()
t=0
for i in range(0,len(str)):
    if(str[i] not in s):
        s.add(str[i])
        c=len(s)
    else:
        s.clear()
        c=0
    t=max(t,c)
    
print(t)
