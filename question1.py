# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# Expected Result : 2



list=['abc', 'xyz', 'aba', '1221']
i=0
temp=0
while i<len(list):
    if list[i][0]==list[i][-1]:
        temp+=1
    i+=1
print(temp)


