# How to find all pairs in an array of integers whose sum is equal to the given number?

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]


i=0
b=[]
while i< len(n):
    if n[i]+n[-i]==number:
        k=(n[i],n[-i])
        b.append(k)
    i+=1
print(b)


