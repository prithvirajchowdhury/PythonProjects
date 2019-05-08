from employee import employee

#Print the Dictionary
print(employee)

#Loop in keys
for i in employee.keys():
	print(i)
#Loop in values
for i in employee.values():
	print(i)
#Loop in items
for x,y in employee.items():
	print(x,y)

#Add new key to the dictionary
employee["sex"]="Male"
print(employee)

#check if key is present
if "sex" in employee:
	print("TRUE")

#Print the length of the dictionary
print(len(employee))

#Remove a key in the dictionary
employee.pop("sex")
print(employee)
