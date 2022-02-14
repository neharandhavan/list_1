# # Write a Code that finds second maximum element from the list and print it.

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=0 
# min=0 
# for i in range(len(numbers)):
#     if numbers[i]>max:
#         min=max
#         max=numbers[i]
#     elif numbers[i] >min and max!=numbers[i]:
#         min=numbers[i]
                        
# print("second max",min)
 



# a=[3,5,-1,4,6,-9,10]
# i=0
# max=a[0]
# b=[]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         b.append(a[i])
#     else:
#         b.append(max)
#     i+=1
# print(b)            




a=[1,1,0,1,1,1,0,1]
i=0
b=[]
while i<len(a):
    c=0
    c1=0
    j=0
    while j<len(a):
        if a[j]==0 and j<i:
            c+=1
        if a[j]==1 and j>=i:
            c1+=1
        j+=1
    c1+=1
    b.append(c)
    i+=1
print(b)                