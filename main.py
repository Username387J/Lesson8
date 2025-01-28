fruits=["banana","grape","apple","orange","avocado"]
print(fruits)
print(type(fruits))


students=("Jeff","Sophia","Andrew","Jacob",)
print(students)
print(type(students))

#careful of which brackets one uses: []= list, ()=tuple
#Packing - THe proccess of assigning values to a tuple is know as packing
address= (582, "Glasbow Apartment", "Calgary", "California",749000)
print(address)
for i in address:
    print(i)



#unpacking-Unpacking tuples assigns the object in a tuple to multiple variablrs.

houseno, apartment, city, state, pin = address
print("house number: ",houseno)
print("Apartment: ",apartment)
print("State: ",state)
print("City: ",city)
print("PIN: ",pin)

#Tuple can be written without parentheses
accounts= "ST101", "ST859", "STU396"
print(type(accounts))

#Nested tuple- A tuple inside anouther tuple
myTuple = ("mouse",(1,2,3),[10,45,60])
print(type(myTuple))
print(myTuple[0])
print(myTuple[0][3])
#tuple immutable- you cannot change the value of a tuple

#myTuple[0][3]="l"
#print(myTuple)

my_tuple1= ("cat","dog")
my_tuple2= ("rat","hamster")

#concatenation- The combination of tuples
solution = my_tuple1 + my_tuple2
print(solution)
print(len(solution))

#repeats the tuple 3 times
print(solution*3)

#Slicing operator: always add a digit more
tuple1=('C','O','D','I','N','G')
print(tuple1[0:3])
print(tuple1[2:6])

print(tuple1[:3])
print(tuple1[2:])