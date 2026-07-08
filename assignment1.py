#Q1. Add two Numbers
a = 5
b = 7
addtwonumbers = a + b
print(addtwonumbers)

#Q2.Find if the conditions are obey or not.
a = 5
b = 7
if(a<10 and a>b):
    print("True")
else :
    print("false")

#Q3.Check the conditions
a = 20
b = 50
if(a%10 == 0 and b%10 == 0):
    print("true")
elif(a%10 ==0 or b%10 == 0):
    print("true")
else :
    print("false")

#Q4. find the first digit of a 4 digit number
N = 1234
first_digit = int(str(N)[0])
print(first_digit)

#Q5. find the last digit of a 4 digit number
N = 1234
last_digit = N % 10
print(last_digit)

#Q6. find the remainder
N = 1234
remainder = N % 10
print(remainder)

#Q7. multiply two numbers
a = 5
b = 6
multiply = a * b    
print(multiply)

#Q8.Marks calculator
Science = 80
Maths = 90
English = 70
Total = Science + Maths + English
print(Total)

Average = Total / 3
print(Average)
