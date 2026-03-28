#DICTIONARIES: Dictionaries are used to store the Data In KEY:VALUE Pairs
#Dictionaries are mutable ,but cannot Stor Duplicate Keys 

Dict = {"Name":"Mudasir"}
print(Dict) 
print(Dict["Name"])

#Academic records 
Student = {"Name":"Arfad",
           "Roll no.":"28",
           "Specialisation":"Bsc Nursing",
           "Subjects":{"Anatomy":100/75,
           "Physiology":100/85,
           "Zoology":100/90,
           "Botany":100/75
     }
  }
print(Student.keys())
print(Student.values())
print(Student.get("Subjects"))
print(Student.items())
print(Student["Name"])
Student["Roll no."] = "27"
print(Student["Roll no."])
print(list(Student.values()))
print(len(Student))
Student["Attendence"] = ["Shortage"]#we can add KEY : VALUE ,pair in the dictionary at any time,As we know its a mutable
print(Student["Attendence"])

D_Arizo = {"Name":"Aarizo",
           "Sex":"Girl",
           "Age":22,
           "Profession":"Teacher",
           "M_Status":"Unmarried",
           "EDU_status":["RPS","BANAAT"],
           "Specialisation":"Islamic Studies",
           "Languages":("Arabic","English","Urdu"),
           "Hobbies":("Watching both Cringe & Valuable content"),
           "Address":"Badampoora,Ganderbal",
           "Passion":"Making Frames",
           "Dream":"To Become The Islamic Scholar",
           "Stream":{"Arts":(11,12,),
                     "Islamic Studies":"Graduation"},
          "I called her":["Tarizo","Chudail"],
          "Mood":("Short Tempered","Sometimes Act like i don't Care","Sometimes Act as fragile ,lekin ho/t toh chudail he tum")

           }
print(D_Arizo["Age"])
print(D_Arizo["EDU_status"])
print(D_Arizo["Stream"]["Arts"])
print(D_Arizo["I called her"][1])
print(D_Arizo["Mood"][0])
print(D_Arizo["Languages"][1])
print(D_Arizo["Hobbies"][0])
print(D_Arizo["Specialisation"])
print(D_Arizo["Passion"])
print(D_Arizo["Dream"])
print(D_Arizo["Address"])
print(D_Arizo["M_Status"])
print(D_Arizo["Profession"])
print(D_Arizo["Sex"]) 
print(D_Arizo.get("Name"))  
print(D_Arizo.get("Age"))
print(D_Arizo.get("EDU_status"))
print(D_Arizo.get("Stream"))
print(D_Arizo.items())
print(D_Arizo.get("I called her"))
print(D_Arizo.keys())
print(D_Arizo.values())
print(len(D_Arizo))
print(list(D_Arizo.values()))
print(D_Arizo["Mood"][2])
D_Arizo.update({"Address":["larsun(BIRTH PLACE)","Badampoora(LIVING PLACE)","Ganderbal(DISTRICT)"]})
print(D_Arizo["Address"][0]) 

print(D_Arizo["Address2"])#it will give an error because the key is not present in the dictionary,thats why we use get command to avoid the error and it will return None if the key is not present in the dictionary
print(D_Arizo.get("Address2"))#it will return None if the key is not present in the dictionary
  
print(D_Arizo["Name"])#it will give the value of the key "Name" which is "Aarizo"

##SET : it is a collection of unique items, it is unordered, but it cannot store duplicate items n/ its elements are immutable but the set itself is mutable
Set = {1,2,5,5,6,8,910,9}
print(Set)
print(type(Set))

null_set = set()#it is an empty set
null_set.add(3)
null_set.add(6)
null_set.add(5)
null_set.add(5)
print(null_set)

s_z =  {3,4,5,7,8,9,9,10,5}
s_z.remove(5)
print(s_z)

s1 = {3,4,5,7,8,9,9,10,5}
s1.clear()
print(s1)

s2 = {3,4,5,7,8,9,9,10,5}
s2.pop()
print(s2)
s2.pop()
print(s2)

x = set()
x.add((3,4,60,12,11,34,12,11,4))
print(x)
x.update([3,4,60,12,11,34,12,11,4])
print(x)
x.update([30,30.9,"me"])
print(x)

sx = {9,96,89,90,56,3,6,3,56,8,9}
sx3 = {3,4,10,89,7,56,90,}#union write the common elements once not twice ,because set is collection of unique elements 
print(sx.union(sx3))

sx = {9,96,89,90,56,3,6,3,56,8,9}
sx3 = {3,4,10,89,7,56,90,}#intersection gives the common Elements
print(sx.intersection(sx3))

Dict = { }

v = int(input("Enter the marks of physics:  "))
Dict.update({"physics": v },)

v = int(input("Enter the marks of chemistry:  "))
Dict.update({"chemistry": v },)

v = int(input("Enter the marks of maths:  "))
Dict.update({"maths": v },)
print(Dict)

subjects = {"python", "Java", "C++", "python", "C", "Java", "Javascript", "C++"}
print(list(subjects))
print(f"total number of classes required: {len(subjects)}")

dictionary = {"Table": ("a piece of furniture", "list of facts & figures"),
               "Cat":["A small Animal"]}
print(dictionary)

y = set()
y.update([9,9.0])
y.add("9.0")#to add the 9.0 separately we must have to use the string data type,otherwise set can take it as one element 
print(f"{y,type(y)}")

