# pairring
      

a=[1,2,3]
i=0
b=[]
while i<len(a):
    j=0
    while i>j:
        if a[i]+a[j]:
            b.append([str(a[i])+str(a[j])])
        j=j+1
    i=i+1
print(b)
