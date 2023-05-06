number= 55
number2 = str(number)
print(number2)
print('number is '+ number2)
print(round(100.4))
radius = float(input('Enter the radius of the circle: '))
area = 3.14 * radius ** 2
print('The area of the circle is :', area)
name = input('Enter your name: ')
age = input('Enter your age: ')
print('Your name is '+ name + ', and your age is '+ age )
sentence = input('Enter your sentence: ')
print('Your sentence is ' + sentence)
word1 = input('Enter the word you want to replace: ')
word2 = input('enter the word you want to replace it with: ')
print(sentence.replace(word1,word2))


list1 = [1,2,3,4,5]
list2 = ['Tarun ', 'Tushar','Nakul','valorant','Pubg']
list1.extend(list2)
print(list1)


list1 = [2,7,3,4,5]
list2 = ['Tarun ', 'Tushar','Nakul','valorant','Pubg']
list1.sort()
print(list1)    

def greetings_function(name):
    print('WELCOME'+name)

greetings_function(' Tarun Nair')    

