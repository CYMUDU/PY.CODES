#LIST: Built in data Type That can store set of values,It can store different types of elements
#including (string,float,integer),and its mutable also
 
General_L = ['Mudasir', 20.0, 6,]
print(General_L)
print(General_L[0])


Marks = [56, 90, 40,35, 45, 60,]
print(Marks[0])
print(len(Marks))

#Mutable List
Marks = [56, 90, 40,35, 45, 60,]
Marks[3]= 70 #while doing changes in the list, must remember that you have change the index of a particular value,instead value itself
print(Marks)

#Slicing
L_x = [2, 4, 6, 8, 90, 10, 11, 12, 16]
print(L_x[0:5:2])
print(L_x[0:6])
print(L_x[3:7:3])
print(L_x[0:len(L_x)])
print(L_x[0: :3 ])
print(L_x[2:17:])
print(L_x[:])
 
#NEGATIVE SLICING
xs = [2, 4, 6, 8, 90, 10, 11, 12, 16]
print(xs[-2:-4])#As we know in Python Language, Positive slicing is by default ,so it must to decrement (-) value in place of stepping .
print(xs[-4:-2])
print(xs[-6:-2:1])
print(xs[-6:-2:2])#correct form 
print(xs[-6:-2:-2])#here negative decrement wont work because your moving towards positiv,and by default python adds +1
print(xs[-3:-7:-1])
print(xs[-3:-9:-2])#in negative indexing if you wan to go from lower to upper element use (-)decrement 


#ESSENTIAL METHODS OF LISTS
xs1 = [2, 4, 6, 8, 90, 10, 11, 12, 16]
xs1.sort(reverse = True)
print(xs1)
xs1.append(13)
print(xs1)
xs1.remove(4)
print(xs1)
xs1.insert(4,31)
print(xs1)
xs1[6] = 15
print(xs1)
print(xs1,xs1[3])
xs1.sort()
print(xs1)
xs1.pop()
print(xs1)
xs1.reverse()
print(xs1)
print(type(xs1))
xs1.pop(3)
print(xs1)


#TUPLE: BUILT IN DATA TYPE THAT lets us create immutable sequence of values 

z = (4,5,6,4)
print(type(z))
print(z[0])
print(z[3])
print(z.index(4))
print(z.index(6))
print(z.count(5))
print(z.count(4))
print(z[0:2])#slicing works hers , same as like lists and strings 
# z[1] = 10
# print(z)#As We know the Tuple Is The immutable Built in Data Type 

#Just one comma makes the difference gere ,z1 is str and z2 is Tuple
z1 = (4)
print(type(z1))#as pythone acts as int by default

z2 = (6,)
print(type(z))#By commas data type gets changed 

#PRACTICE QUESTIONS
Movies = [] 
movie1 = input("Enter the name of ist movie: ")
movie2 = input("Enter the name of 2nd movie: ")
movie3 = input("Enter the name of 3rd movie: ")

Movies.append(movie1)
Movies.append(movie2)
Movies.append(movie3)

print(Movies)

#2nd method
Moviez = []
Moviez.append(input("Enter the Name of 1 movie: "))
Moviez.append(input("Enter the Name of 2 movie: "))
Moviez.append(input("Enter the Name of 3 movie: "))
print(Moviez)

lst = [ 1,2,3,2,1]

copy_lst1 = lst.copy()
copy_lst1.reverse()

if copy_lst1 == lst:
    print('palindrome')#palindrome mean the reading the word from both the sides with the same pronunciat
else:
    print('not palindrome')
       

Grades = ("D", "C", "C", "F", "A", "A", "D", "B", "A", "B",)
print(f"The Number Of Students With Grade A are: {Grades.count('A')}")

Grades = ("D", "C", "C", "F", "A", "A", "D", "B", "A", "B",)
Grades1 = []
Grades1.append(Grades)
print(Grades1)

Grades = ["D", "C", "C", "F", "A", "A", "D", "B", "A", "B",]
Grades.sort()
print(Grades)