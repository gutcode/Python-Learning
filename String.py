type (a) #gives the type of variable

mystring = "Hello World"
mystring[1] #Output e (it gives the value of the sequence of the variable)
mystring[-1] #Output o

mystring = 'abcdefghijklmnopqrst'
mystring[4:] #Output 'efghijklmnopqrst'
mystring[4:7] #Output 'efgh'
mystring[::] #Output 'abcdefghijklmnopqrst'
mystring[::3] #Output 'adgjmps'
mystring[::-1] #Output 'tsrqromnlkjihgfedcba' IT REVERSE THE STRING

last_letter = mystring[4:] #Output 'efghijklmnopqrst' YOU CAN PUT VARIABLE THIS WAY AS WELL

letter = 'z' 
letter * 8 #Output zzzzzzzz

x = 'Hello World'
x.upper() #Output HELLO WORLD
x.lower() #Output hello world
x.split() #Output ['Hello', 'World']
x.split(e) #Output ['H','llo','World']


my_name = 'Jose'
print("Hello" + my_name) # Output Hello Jose
my_name.format() #Output Jose

print('This is a string {}'.format('Inserted')) #Output This is a string Inserted
print('The {3} {4} {1} {2} {0}'.format('lady', 'in', 'that', 'dress', 'is beautiful')) #Output The dress is beautiful in that lady

result = 100/888
print("The result was {r}".format(r=result)) #Output The result was 0.11261261
print("The result was {r:1.3f}".format(r=result)) #Output The result was 0.113

#New version of format
name = "Jose"
print(f'Hello! My name is {name}') #Output Hello! My name is Jose
tree = "Cactus"
print(f'That is a different type of {tree}') #Output That is a different type of cactus
name = "Sam"
age = 22
print(f"{name} is {age} years old.{name}'s sister is also {age}.") #Output Sam is 22 years old. Sam's sister is also 22.

name = 'Sam' 
age = [25, 23]
print(f"{name}'s {age[1]} age is smaller than his {age[0]} older brother")

#List in Python
mylist = [1,2,3]
len(mylist) #Output 3 LENGTH OF LIST
mylist[0] #Output 1
mylist[1:] #Output [2,3]
anotherlist = [4,5]
totallist = mylist + anotherlist # Output [1,2,3,4,5]
totallist[1] = '1.99'
totallist #Ouput [1,1.99, 3, 4, 5]

#Add items in list
totallist.append(6) 
totallist #Output [1,2,3,4,5,6] Adds at the ends
totallist.pop() #Output 6 REMOVES at the end 
totallist #Output [1,2,3,4,5]

newlist = [3,1,2,5,4]
newlist.sort() #Output [1,2,3,4,5]
newlist #Output [1,2,3,4,5]

newlist.sort() #[1,2,3,4,5]
mysortedlist = newlist
mysortedlist #Output [1,2,3,4,5] GIVING ANOTHER VARIABLE NAME

listing = [1,2,3,4]
listing.pop() #Output 4
listing #Output [1,2,3]

#DICTIONARY

my_dict['key':'value','key2':'value2']

price_lookup = {'apple':1, 'Orange': 2, 'Lemon': 3}
price_lookup['apple'] #Output 1

#OLDER STYLE OF OVERWRITING FILE
%%writefile babu.txt                #Output writing file
This is a first line
This is another line which is second
THis is a last and third one

babu = open('babu.txt')    #No Output
babu.read() #Provide a single sentence with contents on it
babu.seek(0) #Sets the new position of variable
babu.read() #You can read again after the seek usages

#NEWER STYLE OF OVERWRITING FILE

with open('babu.txt') as f:             #f is an variable here
  contents = f.read()                   #You won't need to use seek after this since it closes itself
  
  
with open('babu.txt', mode = 'w') as f:
  f.write('I created this file somereasons') #It overwritet the file with the sentense as shown 
  
withopen('babu.txt', mode = 'r') as f:
  print(f.read())             #It then after the overright, you would need to always command the line with read and mode as r
  

  



