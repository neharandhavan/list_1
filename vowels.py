# vowels

a='neha'
v='aeiou'
count=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j] in v:
            count+=1
            print(a[i][j])
        j+=1
    i+=1
    
print(count)


