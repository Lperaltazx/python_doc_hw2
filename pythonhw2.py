
#string manipulation

#.lstrip()
name = 'zking luis'
print(name.lstrip(" " "z"))

#.rstrip
name = 'king zahrtexh'
print(name.rstrip(" " "h"))

#.strip()

name = 'king zahrtex'
print(name.strip())

#string exercise
names = ['   zeLDa', 'link', ' gAnon ', 'BATMAN']
for name in names:
    print(name.strip().upper())

#working with list

#min()

my_list = [1, 5, 6, 8, 4, 9]
print(min(my_list))

#max()
my_list = [1, 5, 6, 8, 4, 9]
print(max(my_list))

#sum()
my_list = [1, 5, 6, 8, 4, 9]
print(sum(my_list))

#sorted()

my_list = [1, 5, 6, 8, 4, 9]
print(sorted(my_list))
print(my_list)

#.sort()
my_list = [1, 5, 6, 8, 4, 9]
my_list.sort()
print(my_list)

#copying a list

my_list = [1, 5, 6, 8, 4, 9]
print(my_list[:3])
print(my_list[::-1])

#in keword

l_characters = ['link', 'zelda', 'ganon', 'majoras']

if 'link'  in l_characters:
    print('is a hero')
else:
    print('Not the hero')

#not in keyword

l_characters = ['link', 'zelda', 'ganon', 'majoras']

if 'link' not in l_characters:
    print('is a hero')
else:
    print('Not the hero')

#checking an empty list

l_1 = []
if l_1:
    print('YES')
else:
    print('nope')

#removing instance with a loop

namelist = ['zack', 'zelda', 'link', 'ganon']

while 'zack' in namelist:
    namelist.remove('zack')
print(namelist)

#list exercise
names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

my_list = []
for name in names:
    if name not in my_list:
        my_list.append(name)
print(my_list)


#list comprehension

numbers = []

for i in range (100):
    numbers.append(i)
print(numbers)
print('\n')

num_comp = [i for i in range(100)]
print(num_comp)

# square number comprehension

squar = [i**2 for i in range(15)]
print(squar)

#string comprehension

food = ['sushi', 'tacos', 'ramen', 'pizza']
first_char_comp = [foods[0] for foods in food]
print(first_char_comp)

#if statements --> if always come after the for

f_names = [food for food in food if food[0] == 's']
print(f_names)

#tuples
my_tuple = (1, 2, 3, "hello", 4.56)

print(my_tuple[0])
print(my_tuple[3])

print(len(my_tuple))

#sorted

my_tuple = (3, 1, 5, 2, 4)

sorted_list = sorted(my_tuple)
print(sorted_list)

#adding values
my_tuple = (1, 2, 3)

new_tuple = my_tuple + (4, 5)

print(new_tuple)

#functions

def sayhi():
    return "hello world"
print(sayhi())

#accepting parameters

def fullName(f_name, l_name):
    return f'hi {f_name}, {l_name}'
print(fullName('luis', 'peralta'))

#default parameters

def printName(first, last='peralta'):
    return f'the name is {last}...{first} {last}.'
print(printName('luis'))

#making an argument optinal

def printNextName(first, middle='', last='ed'):
    return f'hello {first} {middle} {last}!'
print(printNextName('mr'))

#keyword arguments

def comicHero(name, powers='flying'):
    return f'{name} and deadpool are {powers}!'
print(comicHero('batman'))

#creating a start, stop, step function 

def my_range(stop, start=0, step=1):
    for i in range(start, stop, step):
        print(i)
    my_range(20, 1, 2)

#returning values
def addnums(num1, num2):
    return num1 + num2

def multinums(num1, num2):
    print(num1 * num2)

multinums(2, 2)
print(multinums(addnums(2, 2), addnums(1, 1)))

#*arg

def printargs(num1, *args, **kwargs):
    print(num1)
    print(args)
    for arg in args:
        print(arg)

    for kwarg in kwargs:
        print(kwarg)

printargs(90, 'luis', 'steve', 'bob', 6, 9, test1='halo', test2='horns')

#docstring

clas_list = ['steve', 'luis', 'link']
def clans(c_list):
    "clan(c_list) function that print out name for everyone in the clan list. clan list is passed in as parameter c_list."
    for name in c_list:
        print(names)


#using a user function in a loop
def printInput(answer):
    print(answer)
response = input('quit')

while True:
    ask = input('what shall be thy game')

    printInput(ask)

    response = input('get ready')
    if response.lower() == 'quit':
        break


#function exercise
first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

both_names =[]
for i in range(len(first_name)):
    print(i)
    both_names.append(first_name[i] + ' ' + last_name[i])
    print(both_names)

#scope
global_var = 20

def example_funcion():
    local_var = 10
    print('inside the function - local variable:', local_var)
    print('inside the function - global variable:', global_var)

example_funcion()

print("outside the function - global variable:", global_var)


#exercise 1

l_1 = [1,11,14,5,8,9]
l_mine = []

for l in l_1:
    if l < 10:
        l_mine.append(1)
print(l_mine)

#exercise 2
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

print(sorted(l_1 + l_2))