# %% [markdown]
# # Python ka Chilla with #baba_aammar
# ## How to use Jupyter Note Book
# ## Basics of Python
# ### **01- My first program**
# 

# %%
print(2+3)
print("Hello World")
print("We are learning python with Aammar")

# %% [markdown]
# ### **02- Operators**

# %%
print(2+1)
print(3-1)
print(6/2)
print(2*3)
print(13%2)
print(6//2)
print(2**3)

print(3**2/2*3/3+6-4)



# %% [markdown]
# *PEMDAS
# Parenthesis Exponents Multipilication Division Addition Substraction 
# left to right sequance for M D & A S*

# %% [markdown]
# ### **03- Strings**

# %%
print("Hello World")
print("We are learning python with Aammar")
print('test for single quotes')
print("test for double quotes")
print('''test for triple quotes''')

print("what's up?")

# %% [markdown]
# ### **04- Comments**

# %%
print("How are you?")                    #press (Ctrl+/) to comment out
print("We are learning python Aammar")   #print a sting
print(2+6) 

# %% [markdown]
# ### **05- Variables**

# %%
fruit_basket = 8
fruit_basket= "Mangoes"
print(type(fruit_basket))
print(fruit_basket)

# %% [markdown]
# ### **06- Input Variables**

# %%
fruit_basket= "Mangoes"
print(fruit_basket)

#input function
fruit_basket= input("what is your favourite fruit?")
print(fruit_basket)

#input function of second stage
name= input("What is your name?")
greetings="Hello!"
print(greetings, name)

#another way of stage 2 input function
name= input("What is your name?")
print("Hello!",name)

#3rd stage input function
name=input("What is your name")
age= input("How old are you? ")
Greetings="Hello!"

print(Greetings, name, ", You are still young")

# %% [markdown]
# ### **06- Conditional Logics**

# %%
# logical operators are either true or false , yes or no , 0 or 1
# equal to                              =
# not equal to                          !=
# less than                             <
# greater than                          >
# less than and equal to                <=
# greater than and equal to             >=

# is 4 equal to 4?
print(4==4)
print(4!=4)
print(3<6)
print(3>6)
print(3<=5)
print(5>=4)

# application of logical operators 
# hammad_age=4
# age_at_School=5
# print(hammad_age==age_at_School) 

# input function and logical operator
age_at_School=5
hammad_age= input("How old is hammad?5")   #input function
#hammad_age=int(hammad_age)
print(type(hammad_age))
print(hammad_age==age_at_School)         #logical operator 


# %% [markdown]
# ### **08- Type Conversion**

# %%
x= 10               #integer
y= 10.2             #float
z= "Hello!"         #string

#implicit type conversion
x= x+y
print(x,"type of x is:", type(x))

#explicit type conversion 
age=input("What is your age?")
age=int(age)
print(age, type(int(age)))

#name
name=input("What is your name?")
print(name, type(str(name)))

# %% [markdown]
# ### **09- If, elif and else**
# 

# %%
hammad_age=2
required_age_at_school=5
# question: can hammad go to school

if hammad_age==required_age_at_school:
    print("Congratulation! Hammad can join the school.")
elif hammad_age > required_age_at_school:
    print("Hammad should join higher secondary school")
elif hammad_age <=2:
    print("You should take care of Hammad he is still a baby")

else: 
    print("Hammad can not go to school")

# %% [markdown]
# ### **10- Functions**

# %%
# definig a functions
# 1
from typing import Text


def print_condenics():
    print(" We are learning with Aammar")
    print(" We are learning with Aammar")
    print(" We are learning with Aammar")

print_condenics()

# 2
def print_codenics():
    text = "We are learning with Aammar in codenics youtube channel"
    print(text)
    print(text)
    print(text)

print_codenics()

# 3
def print_codenics(text):
    print(text)
    print(text)
    print(text)

print_codenics("We are learning with Aammar in codenics youtube channel")

# defining a fuction with if, elif and alse statements

def school_calculator(age):
    if age==5:
        print("Hammad can join the school")
    elif age>5:
        print("Hammad should go to higher school")
    else:
        print("Hammad is still a baby")

school_calculator(2)


# defining a function of future

def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

future_predicted_age=future_age(18)
print(future_predicted_age)

# %% [markdown]
# ### **11- Loops**

# %%
# While and For loops
#while loops

x=0
while (x<5):
    print(x)
    x=x+1

#for loops

for x in range(4, 11):
    print(x)

# array
days = ["Mon", "Tue","Wed","Thu","Fri","Sat","Sun"]

for d in days:
    if (d=="Fri"): break      # loop stops
    if (d=="Fri"): continue     # skips d
    print(d)

# %% [markdown]
# ### **12- Import libraries**

# %%
# if you want to print the value of pi

import math 
print("The value of pi is", math.pi)

import statistics

x=[150, 250,350,450]

print(statistics. mean(x))

# %% [markdown]
# ### **13- Trouble Shooting**
# 

# %%
#print(We are learning python with Aammar)       #without inverted commas is called syntax error

#print(25/0)                                      #Runtime error or zero divison error 


name= "Aammar"
print("Hello name ")                             #Symentic error 
print("Hello", name)   



