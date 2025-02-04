tuple_list = []

for i in range(5)
    print("Enter something into the tuple with commas:")
    #Included a varibale bcause i did not know of any alternatives
    myInput = input() 
    tuple_values = tuple(myInput.split(","))  
    tuple_list.append(tuple_values)  

print("\nThe list of tuples is:")
print(tuple_list)