
#STRINGS : String is a Data type That can store Sequence Of Characters .

str1= "Hey Mudasir , I am here to \n to help you "#\n it simply write your code to the next line 
str2 = " " "but you have\tto be focused"#\t it  a space between elements 

sum = str1 + str2 
print(sum)
print(str1)
print(str2)

name = ("Mudasir" + "Bashir") #concatenatoin 
print(name)
name1 = ("Mudasir" +" " + "Bashir") #Here we can count an Empty space also in the strings 
print(name1)

#THERE ARE MULTIPLE FUNCTIONS OF STRINGS BUT SOME ARE ESSENTIAL :

x3 = "This is my Mechanical Keyboard"
print(x3.endswith("ard"))
print(x3.count("o"))
print(x3.find("my"))
print(x3.capitalize())
print(x3.replace("This", "Yeah "))
 

#INDEXING : it means counting the elements from "0"
x = "Building Skill"
print(x[0])
print(x[3])
print(x[8])

x1 = "Building"
x1[2] = "e"
print(x1)# An error occured ,because strings are not mutable(change)as like lists

#SLICING : cutting of elememts either in strings /Lists 
slc1 = ("The Editor")
print(slc1[2:6]) #excluding 6th index ,as its a rule 
print(slc1[0:len(slc1)])#to the length  of the string 
print(slc1[5:len(slc1)])
print(slc1[0:])#py understands it by default
print(slc1[3:7:2])#start - stop(excluding the 7th Element ) -gaps 

#NEGATIVE SLICING ,elemants start from -1 ,but the fact is  there is no negative slicing in python actually ,its by default 
slc2 = ("The Editor")
print(slc2[-7:-2])
print(slc2[-6:len(slc2)])
print(slc2[-7:-2])
print(slc2[-7:-1:2])
print(slc2[-7:-2:-2])# will give an output the empty list,because for negative steps,start index should be greater than stop index.

#CONDITIONAL STATEMENTS ,HERE THE GAME OF LOGICAL THINKING BEGINS ACTAULLY (IF/ELIF/ELSE statement )

hours = int(input("Enter the physical Cycle of the day: "))

if (hours > 24 and hours <= 48):#48 hours of cycle without/with night /normal day as we regularly see
    life = "humans will start falling under Endangered species" #Threat to Existence if 24 hour cycle gets influenced 
elif(hours<= 24):
    life = "nothing will change except the Ecosystem"#live normal life 
else:
    life = "The brutal Disaster Will Come Soon" #The Planet Earth gets chhanged ,revolution /rotation? 

print("what would happen in the univers: ", life)

x = (input("Enter The Akshit's citizen ship: ")).lower()
Expected_citizenship = "indian"
Nationality = input("Does have a valid Nationality Document?(yes/no): ").lower()
P_nationality = (Nationality == "yes") #it will convert input to a bolean T/F

if not P_nationality:
    print("police has the Authority to Arrest him under section 39BNSS")
elif x == Expected_citizenship and P_nationality:
    print("He has the Indian citizen Ship")
else:
    print("For now he is not an Indian ? Verification is under way")