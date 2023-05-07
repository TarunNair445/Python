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
        
