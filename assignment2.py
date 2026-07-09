#Q1.Find Grades
M = int(input("Enter Marks: "))
if(M<=10):
    print("E")
elif(11<=M<=20):
    print("D")
elif(21<=M<=30):
    print("C")
elif(31<=M<=40):
    print("B")
elif(41<=M<=50):
    print("A")

#Q2.Get Value
C = input("Enter a character: ")
if(C == "p" or C == "P"):
    print("PrepBytes")
elif(C == "z" or C == "Z"):
    print("Zenith")
elif(C == "e" or C == "E"):
    print("Expert Coder")
elif(C == "d" or C == "D"):
    print("Data Structure")

#Q3.find the maxiumum out of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b) 
elif(c>a and c>b):
    print(c)
elif(a==b==c):
    print(-1)

#Q4. find the second smallest
x = 25
y = 12
z = 23

if (x != max(x,y,z) and x != min(x,y,z)):
    print(x)
elif (y != max(x,y,z) and y != min(x,y,z)):
    print(y)    
else:
    print(z)

#Q5. Check whether the triangle is acute or obtuse
a = 20
b = 140
c = 20

if(a+b+c==180):
    if(a>90 or b>90 or c>90):
        print("Obtuse")
    else:
        print("Acute")
else:
    print("Invalid triangle")



