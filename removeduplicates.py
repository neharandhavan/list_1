# Write a Python program to remove duplicates from a list


# a=[2,3,4,4,5,6,7,7,8,9,9,12]
# dup_items=set()
# uniq_items=[]
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)


a=[2,3,4,5,6,7,8,9,12,6,4,2,2,6,9]
list=[]
i=0
while i<len(a):
    h=a[i] 
    if h not in list:
        list.append(h)
    i=i+1
print(list)

                  