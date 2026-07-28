student={
    #key   : values
    "Name":"Taiba",
    "Age":21,
    "Course":"Python"
}
# # update the whole block
# print(student)
# student.update({
#    "Name":"Taiba Arif",
#    "Age":21,
#    "Course":"Python Course"
# })
# print(student)
# # update the values in single line
# student["Name"]="Eman"
# print(student)
# # add new item 
# student["Insitution"] = "Bano Qabil"
# print(student) 
# # access the value
# print(student["Insitution"])
# print(student["Name"])   
# remove one key value
#student.pop("Age")
#print(student) 
# remove last key value
#student.popitem()
#print(student) 
# print only keys
#print(student.keys())
#print only values
#print(student.values())
#for key in student.values():
    #print(key)
#for key in student:
    #print(key)   
#for key,value in student.items():
    #print(key, ":" , value)  
student2=student.copy()
print(student2)
del student2
print(student2)
  






