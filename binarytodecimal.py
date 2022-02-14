# In this program, if we are given any number in binary form, 
# then we will learn to convert that number in decimal form.xx
# content.


binary_number = [1, 0, 0, 1, 1, 0, 1, 1]

i=0
sum=0
while i<=len(binary_number):
    a=binary_number[-i+1]
    sum=sum+a*(2**i)
    i=i+1
print(sum)


