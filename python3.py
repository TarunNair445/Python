for x in range(100):
    print(x)
else:   
     print('finished looping!!')    
     
My_list =  [
    [1,2,3],
    [4,5,6]
]        
for lists in My_list:
    for row in lists:
        print(row)
        
count_file = open("country.txt",'r')
print(count_file.readline()) 
print(count_file.readline()) 
count_file.close() 

count_file = open("country.txt",'r')
for files in count_file.readline():
    print(files) 
count_file.close() 
        
count_file = open("country.txt",'w')
count_file.write("new text here")
   
class person:
    def __init__(self,name, age):
        self.name =name
        self.age = age
name = input('enter the name:')
age = input('enter the age:')

p1 = person(name,age)
print(p1.name)
print(p1.age)                                       

