question_list = [ "How many continents are there?",  
 "What is the capital of India?", 
 "NG mei kaun se course padhaya jaata hai?"
]


options_list = [

    # pehle question ke liye options

    ["Four", "Nine", "Seven", "Eight"],

    # second question ke liye options

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

    # third question ke liye options

    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]

    ]


# # har ek question ke liye, uski solution key (yeh index nahi hai)

solution_list = [3, 4, 1]
life_line = [[1,3],[2,4],[1,2]]
money = [1000 , 5000 , 10000]
i=0
sum = 0 
count = 0
while i<len(question_list):
    print(i+1,question_list[i])   
    j=0
    while j<=len(options_list):
        print(j+1,options_list[i][j])
        j+=1
    if count<1:
        print("do you want to use life line :")
        s = str(input("enter yes or no🥳:"))
        if s == "yes":
            count+=1
            print(life_line[i])
    else:
        print("you have already used life_line")                                                                                                                                                                                                                                          
    n=int(input("Enter the number🥳:"))
    if n==solution_list[i]:
        sum = sum + money[i]
        print("ur ans is correct " , sum)
    else:
        print("ur ans is wrong game is over!😞" , sum)
        break
    i+=1