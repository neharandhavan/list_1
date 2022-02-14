# average-kitna-hai

# How much is the Average?
# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

i=0
sum=0
sum1=0
even=[]
odd=[]
while i< len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        even.append(elements[i])
        avg = sum/len(elements)
    else:
        sum1=sum1+elements[i]
        odd.append(elements[i])
        avg1 = sum1/len(elements)
    i+=1
print(avg)
print(avg1)






