# MAGIC SQUARE


# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
magic=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i=0
sum=0
sum1=0
sum2=0
while i<len(magic):                       
    colum=0
    while colum<len(magic[i]):
        if sum!=15:
            sum=sum+magic[i][colum]
        elif sum1!=15:
            sum1=sum1+magic[i][colum]
        else:
            sum2=sum+magic[i][colum]
        colum+=1
    i=i+1
print(sum,sum1,sum2)
if sum==sum1==sum2:
    print("its a magic square")
else:
    ("it's not magic square")


