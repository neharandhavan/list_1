# aao-jodein

# Lets Add
# Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0

while i < len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
    else:
        sum1=sum1+elements[i]
    i+=1
print("sum of even:",sum)
print("sum of odd:",sum1)     