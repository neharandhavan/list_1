# # How to iterate on two lists together?
# # Let's say you have two lists of the same length. How will you iterate through both the lists together ?

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# a = zip(students,marks)

# for students,marks in a:

#       print(" %s is %s" % (students,marks))





students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]

length=len(students)
length=len(marks)
Counter=0
while Counter<length:
    print(students[Counter]+str(marks[Counter]))
    Counter+=1
