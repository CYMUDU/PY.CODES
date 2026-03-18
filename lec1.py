#BASICS

print('''This year goona be my prime , wont quite 
   wont stop ,whether its tough or easy i'll make it
      happen''') #Print Is one of the function in the python language that we use to get an output of our code.
print ("hello mudasir")
print("mudasir, age 21", "hey how can i assisst you today")
print(26+3)
print("2=3+7")

#UNDERSTANDING THE CONCEP OF VARIABLES:simply assign any value to varaible that u want to print 
Mace = (''' hey automated computed machine ,there is a lot
    of stuff that you did not complete so far,and this year
    i do not wanna listen any Excuse from you,be ready for penalty''')

print(Mace)

Math1 = (13)
print("Yes Sir, Totale number of chapters in my math:",Math1)

Car_x = (20.22)
print("i purchased that car around,in round figure:", Car_x,"lakh")

Arfad = ( not False )
print("Once Arfad was a Thief ,was continuously stolen My clothes: ",Arfad)

#UNDERSTANDING DATA TYPES : in simmple we can say ,its like checking a Branding Value 
print(type(Mace))
print(type(Car_x))
print(type(Math1))
print(type(Arfad))

#SUM/ADD
x = 1200 
z = 1300
sum = (x + z)
print("their total sum is: ", sum)

#SUB
a = 130000
c = 30000
sub = (a -c)
print("Their total difference is : ",sub)

#TYPES OF OPERATORS:
#Arithematic Operators

x = 4 
y = 5 
print(x + y)
print(x * y)
print(x - y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

#RATIONAL/COMPARISON OPERATORS
x = 4 
y = 5
print(x!=y)#True
print(x==y)#False
print(x<=y)#True
print(x>=y)#False
print(y>x)#True
print(type(x))

#ASSIGNMENT OPERATORS
x = 4 
x += 5
print("x is : ", x)
a = 3
a *=9
x *=3
a *= x
print("a is = ",a)
print("x is ", x)
print("a is = ",a)

x1 = 10 
x1 -=5
print("x1 is = ", x1)

x2 = 20
x2 /=5
print("x2 is = ", x2)

x3 = 25
x3 //=4
print("x3 is = ", x3)

#LOGICAL OPERATORS
a = (not False)
a1 = (not True)
b = (True and True)
c = (True or False)
d = (False or False) 
a1 = 60 
a2 = 40 
print("Their results are as follows : ",(a1 < a2)and (a2 > a1))
print(a)
print(a1)
print(b)
print(c)
print(d)

#TYPE CONVERSION
x =float ("5")
y = int(2.5)
z = str(2.5)
sum = x + y 
print("The sum is : ", sum)
print(type(sum))#here float is a superior than int thats why it shows data type float 
print(type(y))
print(type(x))
print("its the  string , z: ",z)
print(type(z))

#TAKE INPUT FROM USER

mudu = int(input("Enter your IITP card id: "))
print("Thats my ID Number sir: ", mudu, "May i now leave sir")

ph = int(input("Enter your number of phones your purchased: "))
print("i purchased: ",ph,type(ph))

#WAP to take input two number and print their sum

num1 = int(input("Enter the first numnber: "))
num2 = int(input("Enter the Second number: "))
sum = num1 + num2 
print(f"sum of two number num1 & num2 is : {sum}")

# WAP a program to take input sides of Rectangle and Print Their Area

_R1 = int(input( "Enter the length of a rectangle: "))
_R2 = int(input("Enter the height of a rectangle : "))
Area = _R1 * _R2
print(Area)

#WAP a program to take input sides of a Sqaure & Print Their Area

S1 = float(input("Enter the Length of Sides of Square: "))
print(f"Area of a Square: {S1*S1}")




