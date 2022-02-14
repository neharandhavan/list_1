# Kaun Banega Codepati (KBC) - Setup

# Lists ke baare mein seekhne ke liye hum Kaun Banega Crorepati jaise ek 
# game banayenge python ka use kar ke. Yeh code dekh kar samjhe - ki kaise humne KBC game banane ke 
# liye, kuch important cheezein define ki hai - jaise - questions, options aur unke solutions.
 
question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1] 


# lovr


solution_list = [3, 4, 1] 
answer_list=[
    ["(1)four","(3)seven"],
    ["(4)Delhi","(2)Bhopal"],
    ["(4)Agricultue","(1)Software Engineering"]
]
print("kaun Banega codepati (KBC)")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[b][a]
        print(a+1,k)
        a=a+1
    num1=input("do you want 50 50 lifeline::")
    if num1=="yes":
        print("50 50 lifeline")
        if count<1:
            print(answer_list[b])
            num2=int(input("enter your answer::"))
            if num2==solution_list[i]:
                s+=10000
                print("your answer is correct")
                print("you win Rs/",s)
            else:
                print("incorrect answer")
                print("you can,t play again")
                print("you win Rs/",s)
                print("\U0001F629")
                break
            count+=1
        else:
            print("you already use lifeline ::")
            m=int(input("enter your answer :"))
            if m==solution_list[i]:
                print("congrats your answer is right")
                s+=10000
                print("you win Rs/",s)
            else:
                print("No chance")
                print("youe answer is wrong")
                print("you win",s)
                break
    else:
        pass
    k=int(input("enter your answer"))
    if k==solution_list[i]:
        print("right answer")
        s+=10000
        print("you win Rs/",s)
    else:
        print("no chance")
        print("your answer is wrong")
        print("you win Rs/",s)
        print("\U0001F917")

    i=i+1
print("congrulation you are a part of_KON BANAYGA CODEPATI_")
print("you win Rs/",s)
print("THANK YOU BEING PART")   