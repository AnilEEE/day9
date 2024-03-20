# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

'''

#  2.)Find the uncommon words from 2 strings
s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)


# ! constructors
# ? Eg:2
# * unparametarised constructor
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__() 


Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -




# Eg:3
# * Parametarised Constructor
class profile:
    def _init_(self, id, name, age):
        print(id, name, age)
        
obj = profile(1, "sid", 29)


# ? Eg:4
class c1:
    email = "sid@gmail.com"

    def m1(self):
        name = "sid"
        place= "cbe"
        print(name, place)
        print(self. email)

object = c1()
object.m1()


# ? Eg:5
class c1:
    def m1(self):
        name = "sid"
        age = 28
        return name, age
    def display(self):
    print(name, age)
    print(self.name, self.age)
    print(m1())

object = c1()
object.display()




# eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "malli"
        self.email = "malli@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()



# ! Eg:2
# class c1:
#    def _init_(self):
#        print("Iam constructor from parent class")

# class child1():
#    pass

# obj = child1()



# ! Eg:3
class parent:
    name = "sidhu"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()


# ! Eg:2
class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substraction, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)


# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)



class catagory:
    def weight(self, weight):
        print(weight)
    def display(self, color, taste):
        print(color, taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste "neutral taste"
        self.display(color, taste)
class carrot(catagory):
    def carrot_specs(self):
color="green"
taste "sweet"



# heirarichal Inheritance
 #! Heirarical inheritance
class catagory:
    def weight(self,weight):
        print("weight")
    def display(self,color,taste):
        print(color,taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs (self):
        color="green"
        taste= "sweet"
        self.display(color,taste)



#! Heirarical inheritance.
#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
color="green"
LF-321

'''

# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inhertiance

class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")




# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

















        




























































































