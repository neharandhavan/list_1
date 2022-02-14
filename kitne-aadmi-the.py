# kitne-aadmi-the

# How many people were there?
# Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[]
odd=[]
while i< len(elements):
    if elements[i]%2==0:
        even.append(elements[i])
    else:
        odd.append(elements[i])
    i+=1
print(even)
print(odd)
