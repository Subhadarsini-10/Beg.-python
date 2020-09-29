#!/usr/bin/env python
# coding: utf-8

# <ol><p><b>math module</b></p></ol>

# In[3]:


import math
print(round(2.9))


# In[6]:


import math
print(math.ceil(2.9))


# In[7]:


import math
print(math.floor(2.9))


# In[8]:


x=2.9
print(abs(x))


# In[9]:


x=-2.9
print(abs(x))


# <p><b>if statements</b></p>

# In[3]:


is_hot=True
is_cold=True
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
if is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("a wonderful day")


# In[7]:


price =1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    doen_payment=0.2*price
    
print(f"Down payment:",down_payment)


# <p><b>logical operator</b></p>

# In[23]:


has_high_income=False
good_credit=True
if has_high_income or good_credit:
    print("eligible for loan")
    


# In[26]:


has_good_credit=True
has_criminal_records=False
if has_good_credit and not has_criminal_records:
    print("eligible for loan")


# <p> the not operator gives the opposite of the declared statement</p>

# In[9]:


temp=40
if temp>30:
    print("it's a hot day")
elif temp<10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")


# In[30]:


name="subha"
if len(name)<3:
    print("name must be atleast 3 characters")
elif len(name)>50:
    print("it can be a maximum of 50 characters")
else:
    print("the name is beautiful")


# <p><b>Project:Weight converter</b></p>

# In[37]:


weight=int(input('weight:'))
unit=input('(L)bs or (K)g')
if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are {converted} kilos")
else:
    converted=weight//0.45
    print(f"you are {converted} pounds")


# <p><b>while loop</b></p>

# In[3]:


i=1
while i<=5:
    print('*'* i)
    i+=1
print("Done")


# <p><b>guessing game</b></p>

# In[10]:


secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('Guess:'))
    guess_count+=1
    if guess == secret_number:
        print('you won!')
        break
else:
    print('you lost!')


# <p><b>Car game</b></p>

# In[1]:


command=""
started=False
while True:
    command=input(">").lower()
    if command == "start":
        if started:
            print("the car is already started")
        else:
            started=True
            print("car started..")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
        start-to start the car
        stop-to stop the car
        quit-to quit the game
        """)
    elif command =="quit":
        break
    else:
        print("i don't understand")


# <p><b>For Loop</b></p>

# In[3]:


for item in 'python':
    print(item)


# In[7]:


for item in range(2,10,2):
    print(item)


# In[8]:


my_cart=[10,20,30]
total=0
for prices in my_cart:
    total+=prices
print(f"total:",total)
    


# <i>Nested List</i>

# In[10]:


for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


# In[12]:


numbers=[5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)


# In[17]:


numbers=[5,2,5,2,2]
for x_counts in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)


# <p><b>list</b></p>

# In[25]:


name=['subha','sara','fanny','happy']
print(name[2])
print(name[-1])
print(name[1:3])
print(name[:])
print(name[0:])


# <p><b>Write a program to find the largest number in a list.</b></p>

# In[26]:


numbers=[1,3,4,90,64,10]
max=numbers[0]
for number in numbers:
    if number >max:
        max=number
print(max)
        


# In[28]:


numbers=[1,7,4,6,4]
min=numbers[0]
for number in numbers:
    if number < min:
        number=min
print(min)


# <p><b>2D list</b></p>

# In[33]:


matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)


# In[52]:


numbers=[1,4,5,6,8,4]
numbers.append(13)
print(numbers)
numbers.sort()
print(numbers)
numbers.insert(0,7)
print(numbers)
numbers.remove(8)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.count(4))
print(50 not in numbers)


# In[56]:


numbers=[2,3,4,3,4,6,4,3,5,6,5]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


# <p><b>Tuple</b></p>

# In[3]:


number=(1,3,4,7)
print(number)


# <p>in tuple we can't do any kind insert ,append or anything,</p>

# <p><b>unpacking</b></p>

# In[5]:


coordinate=(1,2,3)
x,y,z=coordinate
print(y)


# <p><b>Dictionary</b></p>

# In[9]:


phone=input("Phone:")
digital_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for ch in phone:
    output+=digital_mapping.get(ch,"!")+" "
print(output)


# <p><b>Functions</b></p>

# In[17]:


def greet_user():
    print("hey there")
    print("welcome to india")
    
    
print("start")
greet_user()
print("finish")


# <p><b>Parameters</b></p>

# In[22]:


def greet_user(name):
    print(f"hi {name}")
    print("a warm welcome")
    
    
print("start")
greet_user("subha")
greet_user("fany")
print("finish")


# In[25]:


def greet_user(first_name,last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome back")
    
    
print("Start")
greet_user("subhadarsini", "pattnaik")
print("Finish")


# <p><b>Keyword arguments</b></p>

# In[26]:


def square(number):
    return number*number


result=square(4)
print(result)


# <p><b>exception</b></p>

# <p>without trashing your code to get rid of valueerror just go with try and except</p>
# 1<p>ValueError</p>

# In[29]:


try:
    age=int(input("Age:"))
    print(age)
except ValueError:
    print("invalid value")


# 2<p>ZeoDivisionError</p>

# In[30]:


try:
    age=int(input('Age:'))
    print(age)
    income=2000
    risk=income/0
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')


# <p><b>Constructor</b></p>

# In[63]:


class person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print("talk")
        
        
herry=person("herry smith")
print(herry.name)
herry.talk()


# <p>Create a new type called person,the person object should have name attribute as well as talk.</p>

# In[45]:


class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"Hi,i'm {self.name}")
        
        
john=Person("john smith")
john.talk()

boby=Person("Bobby deol")
boby.talk()


# <p>Inheritance</p>

# In[52]:


class Mammal:
    def walk(self):
        print("walk")
        
        
class dog(Mammal):
    def bark(self):
        print("bark")
        
        
class cat(Mammal):
    def be_annoying(self):
        print("annoying")
        
        
dog1=dog()
dog1.bark()

cat1=cat()
cat1.be_annoying()


# <p><b>Generating random variables</b></p>

# <p>a task to get random values when we roll a dice.Define a class Dice and a function roll along with the tuple</p>

# In[4]:


import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second
    
    
dice=Dice()
print(dice.roll())


# In[6]:


import random

for i in range(3):
    print(random.random())


# In[11]:


import random

for i in range(3):
    print(random.randint(10,20))


# <p><b>Machine Learning</b></p>

# 1-<p>import the data</p>
# 2-<p>claen the data</p>
# 3-<p>split the data into test cases</p>
# 4-<p>create a model</p>
# 5-<p>train a model</p>
# 6-<p>make preictions</p>
# 7=<p>evaluate and improve</p>
# 

# <p><b>Libraries and tools</b></p>

# <p>Numpy</p>
# <p>Panadas</p>
# <p>Matplotlib</p>
# <p>Scikit Learn</p>

# In[ ]:




