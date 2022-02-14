# # kitne-crorepati

# # How many Crorepati?

# # Write a program that tells in the above list that how many people are there in the above list who are :

# # 1 - `Crorepati`
# # 2 - `Lakhpati`
# # 3 - `Dilwale`

# # All those who have money more than or equal to 1 crore are known as Crorepati. All those who have money money greater than or equal to 1 lakh, those are called Lakhpati.
# # Rest of the people are called Dilwale.


kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

Crorepati=[]
Lakhpati=[]
Dilwale=[]

i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        Crorepati.append(kitna_paisa_hai[i])
    elif kitna_paisa_hai[i]>=100000:
        Lakhpati.append(kitna_paisa_hai[i])
    else:
        Dilwale.append(kitna_paisa_hai[i])
    i+=1
print(Crorepati,": Crorepati")
print(Lakhpati,": Lakhpati")
print(Dilwale,": Dilwale")

