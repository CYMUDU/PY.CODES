#LOOP : are used to repeat the instruction in a program until a certain condition is met
#Types of Loops : 1. For Loop 2. While Loop

#while Loop : is used to repeat a block of code until a certain condition is met

nums = 100

x = 1
while x <= nums:
    print(x)
    x += 10


numz = 1

xs = 100
while xs > numz:
    xs-= 1
    print(xs)


n = int(input("Enter a number : "))
    
count = 1 
while count < 10 :
    print(n*count )
    count += 1
    
x2 = [ 4, 16 , 32, 64, 128, 140, 162]

i = 0
while i < len(x2):
    print(x2[i])
    i += 1    

x3 = [ 4, 16 , 32, 64, 128, 140, 162, 32]

z = 32
i = 0
while i < len(x3):
    if x3[i] == z:
        print(f"the number {z} is found at index {i}")
        break
    i += 1
    print(x[i])
   
    

m = (4, 16 , 32, 64, 128, 140, 162, 32)

c = 32
i = 0
while i < len(m):
    if m[i] == c:
        print(f"the number {c} is found at index {i}")
       
    print (m[i])
    i += 1
else:
    print(f"END THE PROGRAM ")


# #iterating through a numbers using for loop
x1 = int(input("Enter the starting number : "))

for i in range (x1):
    if i == 5:
        continue #it will skip the value 5 and continue with the next value
    print(i)


num = [3, 4, 5, 7, 9, 10, 8]

S = 0
for i in num:
    if (i == 7):
        continue #it will skip the value 7 and continue with the next value
    print(i)
    S += 1


even = [12, 45, 34, 16, 23, 17, 18, 20]
for i in even:
    if i % 2 == 0:
        continue #it will skip the even numbers and continue with the next value
    print(i)

odd = [12, 45, 34, 16, 23, 17, 18, 20]
for i in odd:
    if i % 2 != 0:
        continue #it will skip the even numbers and continue with the next value
    print(i)

cx = int(input("Enter a number : "))
for i in range (1, cx+2):
    if i%2 == 0:
            continue #it will skip the even numbers and continue with the next value
    print(i)


n = 8
for i in range (n):
    pass #it will do nothing and continue with the next value
print("its for useful work")

seq = [1, 2, 3, 4, 5]
for i in seq:
    print(i)

#linear searching : is a simple search algorithm that checks each element in a list until it finds the target value or reaches the end of the list
seq1 = [1, 2, 3, 4, 5]

sq = 3
idx = 0 #we not used this inside condition because we want to print the index of the
 #value 3 when we find it in the list, if we used it inside the condition it will not be able to print the index of the value 3 because it will be out of scope
for i in (seq1):
    if i == sq:
      print(f"the number {sq} is found at index {idx}")
      break
          #it will stop the loop when it finds the value 3  
    print(i)
    idx+= 1


Tb = int(input(f"the table of :"))

n1 = 10
for n1 in range (1, 10+1):
    
    print(f"{Tb} x {n1} = {Tb*n1}") 



nxs1 = int(input("Enter a number : "))

sum = 0
for i in range (1, nxs1+1):
    sum += i
print(f"the total sum of number {nxs1} is : {sum}")




nxs = int(input("Enter a number : "))

sum = 0
i = 1
while i <= nxs:
    sum += i 
    i += 1
    print(f"the total sum of number {nxs} is : {sum}")


n = 5
fact = 1
for i in range (1, n+1):
    fact *= i
    print(f"the factorial of number {n} is : {fact}")

n = 5
f = 1
i = 1

while i <= n:
    f *= i
    i += 1
    print(f"the factorial of number {n} is : {f}")




