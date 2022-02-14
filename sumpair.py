# SUM PAIR:

sum=30
a=[10,11,12,13,14,17,18,19]
i=0
b=[]
while i<len(a):
    j=0
    while i>j:
        if a[i]+a[j]==sum:
            b.append([a[i],a[j]])
        j=j+1
    i=i+1
print(b)

