print("###Term 1###")
#ask for the degree they scored in term 1
a1=int(input("AES:"))
m1=int(input("Maths 1:"))
p1=int(input("Physics 1:"))
c1=int(input("Computer Programming 1:"))
#ensure the degree won't more than 100 and less than 0
if a1<0 or m1<0 or p1<0 or c1<0 or a1>100 or p1>100 or c1>100 or m1>100:
    print("That is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 1 is inputted.")


print("###Term 2###")
#ask for the degree they scored in term 2
a2=int(input("AES:"))
m2=int(input("Maths 2:"))
p2=int(input("Physics 2:"))
c2=int(input("Computer Programming 2:"))
#ensure the degree won't more than 100 and less than 0
if a2<0 or m2<0 or p2<0 or c2<0 or a2>100 or p2>100 or c2>100 or m2>100:
    print("That is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 2 is inputted.")

print("###Term 3###")
#ask for the degree they scored in term 3
a3=int(input("AES:"))
m3=int(input("Maths 3:"))
p3=int(input("Physics 3:"))
c3=int(input("Creative Design:"))
#ensure the degree won't more than 100 and less than 0
if a3<0 or m3<0 or p3<0 or c3<0 or a3>100 or p3>100 or c3>100 or m3>100:
    print("That is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 3 is inputted.")

if a3<40 or m3<40 or p3<40 or c3<40 or a2<40 or p2<40 or c2<40 or m2<40 or a1<40 or m1<40 or p1<40 or c1<40:
    print("You failed because the subjects should not less than 40%.")
    quit()

#calculate the average degree of all the subjects
y1=(a1+a2+a3+m1+m2+m3+c1+c2+c3+p1+p2+p3)/4
y2=(m2+m3)/2
#discuss the average and print the comments they should have.
if y1>=60:
    print("Well done :) YOU Progress!!")
elif y1==100:
    print("Wow, you are so amart! 100 in everything!!:)")
elif y1<60:
    print("Sorry, you do not progress because you must have at least an average of 60% overall.")
    quit()
#check the maths
if y2<65:
    print("You failed because of the maths.")
    quit()
#check the AES
if a3<60:
    print("You failed because your AES 3.")
    quit()

quit()