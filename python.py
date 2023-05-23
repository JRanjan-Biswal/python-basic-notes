#  note: python uses # and """ to create comments
'''
print('hello world')
'''

############################################################################################################
# Built-in Data Types
'''
Text Type: 	    str

Numeric Types: 	int, float, complex

Sequence Types: list, tuple, range

Mapping Type: 	dict

Set Types: 	    set, frozenset

Boolean Type: 	bool

Binary Types: 	bytes, bytearray, memoryview

None Type: 	    NoneType
'''

'''
x = "Hello World"  # string
x = 20             # int   : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 20.5           # float : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1j             # complex  : Complex numbers are written with a "j" as the imaginary part:
x = True           # bool
x = None           # none
x = range(6)       # range
x = b"Hello"       # bytes
x = bytearray(5)   # bytearray
x = memoryview(bytes(5))  # memoryview
x = ["apple", "banana", "cherry"]  # list  : A list is a collection of ordered data.
x = ("apple", "banana", "cherry")  # tuple : tuple is a ordered collection of data. They are immutable
x = {"name" : "John", "age" : 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozen set

important link : list vs tuple vs dict vs set : https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python
'''

#   ---- RANDOM NUMBERS -----
# Import the random module, and display a random number between 1 and 9:
'''
import random

print(random.randrange(1, 10)) 
'''

# ---- Strings are Arrays ------
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
'''
a = "Hello, World!"
print(a[1])
'''


# ----  Looping Through a String  ------
# Since strings are arrays, we can loop through the characters in a string, with a for loop.\
'''
for x in "banana":
  print(x)
'''

# ---- String Length -----
# len() : method to get the length of the string
'''
a = "Hello, World!"
print(len(a))
'''

# ------- Check String ------
# To check if a certain phrase or character is present in a string, we can use the keyword in.
'''
txt = "The best things in life are free!"
print("free" in txt)  # "in" is used to check a substring in string // prints True
'''

# Print only if "free" is present: ( IF )
'''
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
'''

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''

# print only if "expensive" is NOT present:
'''
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
'''


# ----------------- SLICING STRINGS ----------------------------
'''
b = "Hello, World!"
print(b[2:5])  # o/p: llo   --> reason : Get the characters from position 2 to position 5 (not included)
print(b[:7])   # o/p: Hello, --> reason : Get the characters from position 0 to position 7 (not included)
print(b[2:])   # o/p: llo, World!, --> reason : Get the characters from position 2 till end of the string

# -- negative indexing --
print(b[-5:-2])  # o/p: orl
'''

# -------------------- MODIFYING STRINGS ------------------------
'''
a = "  HeLlo, WoRld! "

# Upper Case : upper()
print(a.upper())

# Lower Case : lower()
print(a.lower())

# Remove Whitespace : strip()
print(a.strip())   # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Replace String : replace()
print(a.replace("H", "J"))  # o/p: JeLlo, WoRld! 

# Split String : split()
print(a.split(','))  # o/p: ['  HeLlo', ' WoRld! ']
'''

# ------------------- String Concatenation --------------------
'''
a = 'hello'
b = 'world'
print(a+b)
print(a + " " + b)
'''

# ------------------- FOMAT STRING -----------------------------
# We cannot concatenate string with number therefore we use format
'''
age = 23
txt = 'jyoti is {} years old'
print(txt.format(age))
'''

##############  BOOLEANS ############
# ------- returns True ------
'''
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
'''
# ------- returns False ------
'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

########################### LIST #################################
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

# eg. a list
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
'''

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# If you add new items to a list, the new items will be placed at the end of the list.
# lists can have duplicates

##  IMPORTANT: A list can contain different data types ##

# type of list
# From Python's perspective, lists are defined as objects with the data type 'list':
'''
mylist = ["apple", "banana", "cherry"]
print(type(mylist))   # <class 'list'> 
'''

# IMPORTANT: LIST constructor can be used to create a list
# e.g.:
'''
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)
'''

# ------  Range of Indexes ------------
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # o/p: ['cherry', 'orange', 'kiwi']
'''

# ------- Splicing in List ------------
'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
'''

# --------- Insert new Item in list --------
# syntax:-->  list.insert(index, item)
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
'''

# --------- Append new Item in list ----------
# appends new item to the end of the list
# syntax:--> list.append(item)
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
'''

# ----------- Extends list -------------------
# To append elements from another list to the current list, use the extend() method.
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
'''

# IMPORTANT note: The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
'''
thislist = ["apple", "banana", "cherry"]   # list
thistuple = ("kiwi", "orange")             # tuple
thislist.extend(thistuple)
print(thislist)
'''

# ----------- Remove Items for list -----------

# remove() : remove specified item from list
'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
'''

# pop() : takes index, if we do not specify index, it removes last item from list
'''
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
'''

# del : also removes specified item from list and is can also delete complete list
'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)   # o/p: ['banana', 'cherry']

del thislist  # delete list completely\
'''

# clear() : this method clears the list, leaving a empty list
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   # o/p: []
'''

# ----------- Looping through list -----------
# for loop iteration
'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
'''

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
'''
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):   # this creates an iterable like: [0, 1, 2]
    print(thislist[i])
'''

# while loop
'''
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
'''

# Looping Using List Comprehension
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 
'''

# ---------- List Comprehension ------------------
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# SYNTAX : newlist = [expression for item in iterable if condition == True]
# link: https://www.w3schools.com/python/python_lists_comprehension.asp

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# the above mentioned can be comprehended as :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
'''

# ------------- Sorting --------------------------
# List objects have a sort() method that will sort the list alphanumerically, ASCENDING, by default:
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
'''

# sorting in DESCENDING order
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
'''

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# Sort the list based on how close the number is to 50:
'''
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)      # o/p --> [50, 65, 23, 82, 100]
'''

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# therefore we can use this technique to sort
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)     # o/p --> ['banana', 'cherry', 'Kiwi', 'Orange']
'''

# Reverse Order
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)     # this reverse the list
'''

# ------------- Copy List ------------------------
# Important Note:
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# copy() : make a copy of list
'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
'''

# list() : make a copy of list
'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
'''

# VARIOUS BUILT IN METHODS ON LISTS: https://www.w3schools.com/python/python_lists_methods.asp


################################ TUPLE #################################
# e.g.: mytuple = ("apple", "banana", "cherry")
# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable.
# Tuples allow duplicates values

# The tuple() Constructor
# we can use tuple constructor to create a new tuple
'''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
'''

# IMPORTANT: Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# e.g.:
'''
x = ("apple", "banana", "cherry")
y = list(x)      # convert it to list to do the needed changes
y[1] = "kiwi"
x = tuple(y)     # then convert it back into tuple

print(x) 
'''

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
'''

# del to completely delete a tuple
'''
thistuple = ("apple", "banana", "cherry")
del thistuple
'''

# ------------ Destructuring or Unpacking ------------- (destructuring is a word used in JS , whereas in python we call it as unpacking)
'''
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
'''

#  Using Asterisk*
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
'''

# -------------------- LOOPING IN TUPLE --------------------------------
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
'''
# looping in tuple is similar to looping in list . refer the list loop notes above

# -------------------- JOIN IN TUPLE -------------------- this is similar to joins in list . refer the list notes above

# IMPORTANT TUPLE METHODS : https://www.w3schools.com/python/python_tuples_methods.asp


########################################### SETS #########################################
# e.g. myset = {"apple", "banana", "cherry"}
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# duplicates are not allowed in set
# True and 1 are considered same value in set
# set can be created using set constructor
'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''

# ----------------- ADD ITEM TO SET --------------------------------
# add() : to add one item to the set
'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 
'''

# update() : to add items from another set to current set
'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 
'''

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 
'''

# -------------------- REMOVE ITEM FROM SET -----------------------------
# remove() 
'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
'''

# discard()
'''
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")   # this wont throw an error when an item is not available in set. 

print(thisset) 
''' 

# pop() : this removes a random item from the set
'''
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 
'''

# clear() : empties the set
'''
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) 
'''

# del() : deletes the set
'''
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
'''

# ---------------------- JOIN TWO SETS ------------------------
# union() : method that returns a new set containing all items from both sets 
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)    # {1, 2, 'a', 3, 'b', 'c'}
'''


# update() : method that inserts all the items from one set into another
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)    # {1, 2, 3, 'a', 'c', 'b'}
'''

# intersection_update() : method will keep only the items that are present in both sets.
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)    # {'apple'}
'''

# intersection(): method will return a new set, that only contains the items that are present in both sets.
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)    # {'apple'}
'''

# symmetric_difference_update() : method will keep only the elements that are NOT present in both sets
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)   # {'banana', 'google', 'cherry', 'microsoft'}
'''

# symmetric_difference() : method will return a new set, that contains only the elements that are NOT present in both sets.
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) # {'cherry', 'microsoft', 'banana', 'google'}
'''

# IMPORTANT SETS METHODS : https://www.w3schools.com/python/python_sets_methods.asp


########################################### DICTIONARIES ###########################################
# e.g. mydict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# A dict is used to store value in key value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates..
# Dictionary items are ordered, changeable, and does not allow duplicates.
# unordered means --> items does not have defined order, you cannot refer to an item by using an index.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:

# -------------------- ACCESS ITEMS IN DICT -------------------
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]

print(x)     # o/p -->  Mustang
'''

# get() : this gives us access to the item
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")

print(x)     # o/p -->  Mustang
'''

# keys() : returns list of keys in the dictionary
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)   # o/p --> dict_keys(['brand', 'model', 'year'])
'''

# values() : return list of values in the dictionary
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()  

print(x)  # o/p --> dict_values(['Ford', 'Mustang', 1964])
'''

# items() : return each item in dictionary, as tuples in list
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)  # o/p --> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
'''

# --------------- ADD NEW ITEM TO DICT --------------------
'''
car = { "brand": "Ford" }

car["color"] = "white"

print(car) # o/p --> {'brand': 'Ford', 'color': 'white'}
'''

# -------------- UPDATE DICTIONARY -------------------------
# update() : this will update the dictionary with the items from the given argument.
#          : this will also be used to add the item 
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})  # o/p --> {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
'''

# ---------------- REMOVE ITEM - DICTIONARY -----------------
# pop() : removes item with specified key name
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

print(thisdict)  # o/p --> { 'brand': 'Ford', 'year': 1964 }
'''

# popitem() : removes last inserted item, (in versions before 3.7, a random item is removed instead)
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()

print(thisdict)  # o/p --> {'brand': 'Ford', 'model': 'Mustang'}
'''

# del() : removes item with specified key name
#       : also deletes the dictionary completely
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]

print(thisdict)  # o/p --> {'brand': 'Ford', 'year': 1964}
'''

# clear() : empties the dictionary
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()

print(thisdict)  # o/p --> {}
'''


# -------------------- LOOPING IN DICTIONARY --------------------
# normal for loop
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
'''

# looping through value() in dict
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.values():
  print(x)
'''

# looping through keys() in dict
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.keys():
  print(x)
'''

# looping through items() in dict
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x, y in thisdict.items():
  print(x, y)
'''

# --------------------- COPY IN DICTIONARY ----------------------
# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, 
# and changes made in dict1 will automatically also be made in dict2.

# copy() : copying a dictionary
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict)
'''

# dict() : copying a dictionary
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)
'''

# IMPORTANT DICT METHODS : https://www.w3schools.com/python/python_dictionaries_methods.asp



############################################################################################################
# not if case. Note: there should be indentation. A indentation is considered as a block of code
'''
if(5 > 2):
        print('this is if')
'''

#############################################################################################################
# variables : Variables do not need to be declared with any particular type, and can even change type after they have been set.
'''
a = 5
b = 'hello'
b = True
print(a, b)
'''

#############################################################################################################
#  CASTING: variables
'''
x = str(1)
#y = int('hello')  #error: invalid literal for int
y = int(5)
z = float(3)
'''


############################################################################################################
# DATA TYPES : type() function.
'''
x = 5
y = "John"
print(type(x))
print(type(y)) 
'''


############################################################################################################
#   Case-Sensitive  : Variable names are case-sensitive.
'''
a = 4
A = "Sally"
# A will not overwrite a 
'''


############################################################################################################
#  Legal variable names:
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''


# Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''

############################################################################################################
# Python allows you to assign values to multiple variables in one line:
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''

# One Value to Multiple Variables
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''

# Unpack a Collection
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry
'''

############################################################################################################
# ------ GLOBAL VARIABLES  -------
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
'''
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
'''

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)    # o/p --> Python is fantastic

myfunc()

print("Python is " + x)    # o/p --> Python is awesome
'''

# The global Keyword
# If you use the global keyword, the variable belongs to the global scope
'''
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)    # o/p --> Python is fantastic
'''



############################## FUNCTIONS #############################

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# ------------- CREATING A FUNCITON ----------
# In Python a function is defined using the def keyword:
'''
def my_function():
  print("Hello from a function")
'''

# -------------- Calling a Function -------------
# To call a function, use the function name followed by parenthesis:
'''
def my_function():
  print("Hello from a function")

my_function()
'''

# --------------- Arguments ---------------------
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
'''

# ---------------- Parameters or Arguments ------------
# A parameter is the variable listed inside the parentheses in the function definition.
# eg. 
'''
def my_function(fname, lname):  # <--- parameter
  print(fname + " " + lname)
'''

# An argument is the value that is sent to the function when it is called.
'''
my_function("Emil", "Refsnes")   # <--- arguments
'''

# --------------------- Arbitrary Arguments ( *args ) ----------------
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'''

# --------------------- Keyword Arguments ---------------------------
# You can also send arguments with the key = value syntax.
'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''

# ----------------------- Arbitrary Keyword Arguments --------------------
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
'''

# ----------------------- Default Parameter Value --------------------
# The following example shows how to use a default parameter value.
'''
def my_function(country = "Norway"):  # <-- If we call the function without argument, 
  print("I am from " + country)       #     it uses the default value

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
'''

# ----------------------- The pass Statement ------------------------
# function definitions cannot be empty, 
# but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.
'''
def myfunction():
  pass
'''

# ------------------ VERY VERY IMPORTANT --- RECURSION ---------------
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
'''


###################################### LAMBDA #################################### 
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax: 
# lambda arguments : expression

# -------------- Add 10 to argument a, and return the result: -----------------
'''
x = lambda a : a + 10

print(x(5))             # o/p : 15
'''

# ------------- Multiply argument a with argument b and return the result --------
'''
x = lambda a, b : a * b

print(x(5, 6))              # o/p : 30     
'''

# ------------- Summarize argument a, b, and c and return the result ------------
'''
x = lambda a, b, c : a + b + c

print(x(5, 6, 2))                 # o/p : 13
'''

# ------------------------- Why Use Lambda Functions? ----------------------------
# The power of lambda is better shown when you use them as an anonymous function inside another function.
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))     # o/p : 22
'''


############################################## ARRAYS ################################################
# sytax: cars = ["Ford", "Volvo", "BMW"]
# len() : return lenth of the array
# append() : add element to an array    # eg.: cars.append("Honda")

# pop() : removes element from the array
'''
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)   # o/p : ['Ford', 'BMW']
'''

# remove() : method to remove an element from the array.
'''
cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)   # o/p : ['Ford', 'BMW']
'''

# methods for arrays : https://www.w3schools.com/python/python_arrays.asp


###################################### CLASS / OBJECTS ###################################### -- OOPS
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# syntax : 
'''
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)   # o/p : 5
'''

# ----------------------- Self Parameter ------------------------
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# ----------------------------- __init__()  -------------------------
# The example above is a class and object in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)   # o/p : john
print(p1.age)    # o/p : 36
'''

# ---------------------------- __str__() -----------------------------
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)   # o/p : <__main__.Person object at 0x0000017E1AC2DF70>


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)  # o/p : John(36)
'''

# ---------------------------- Object Methods ----------------------
# Objects can also contain methods. Methods in objects are functions that belong to the object.
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
'''



################################################## INHERITANCE ########################################
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# --------------------------- Creating a Child Class -----------------------
''' # this is parent/base class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# creating a child class  --> To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person): 
  pass

x = Student('Jyoti', 'Ranjan')
x.printname()
'''

# ------------------- using __init__() ----------------------
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
'''

# ------------------------------- super() --------------------------------------
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
'''

# ------------------------------- Adding Properties to Student (child class) ------------------
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)    # this inherits all methods of parent to child class
      self.graduationyear = 2019       # here we are adding a new property to Student class
'''

# -------------------------- Adding Method to Student/Child class ---------------------------
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

    
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
''' 


############################################# PYTHON ITERATORS #############################################
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().  

# ------------------------------- Iterator vs Iterable ------------------------------
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
'''
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))       # apple
print(next(myit))       # banana
print(next(myit))       # cherry
'''

# ------------------------------- Strings are Iterable --------------------------------
# Strings are also iterable objects, containing a sequence of characters:
'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))       # b
print(next(myit))       # a
print(next(myit))       # n
print(next(myit))       # a
print(next(myit))       # n
print(next(myit))       # a
'''

# -------------------------------- Looping through Iterator ----------------------------
'''
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
'''

# --------------------------------- CREATE AN ITERATOR ----------------------------------
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# All classes have a function called __init__(), which allows us to do some initializing when the object is being created.
# The __iter__() method acts similar, we can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))     # 1
print(next(myiter))     # 2
print(next(myiter))     # 3
print(next(myiter))     # 4
print(next(myiter))     # 5
'''

# ------------------------------ STOP ITERATION -------------------------------
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

'''


############################################# PYTHON POLYMORPHISM #####################################
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# An example of a Python function that can be used on different objects is the len() function.
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# -------------------------------- CLASS POLYMORPHISM -----------------------------------
# the below class car, boat, plane --> all have move() method in common
'''
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
'''


################################################## PTYHON SCOPE ######################################
# A variable is only available from inside the region it is created. This is called scope.

# ------------------------------------ LOCAL SCOPE ---------------------------------
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# A variable created inside a function is available inside that function:
'''
def myfunc():
  x = 300
  print(x)

myfunc()
'''

# ------------------------------------- GLOBAL SCOPE ---------------------------------
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
'''
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
'''

# ------------------------------------- NAMING VARIABLE ----------------------------------
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
'''
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
'''

# ------------------------------------- GLOBAL KEYBOARD -----------------------------------
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
'''
def myfunc():
  global x
  x = 300

myfunc()

print(x)
'''


################################################### PYTHON MODULES #########################################
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# ---------------------------- CREATING A MODULE ---------------------------
# To create a module just save the code you want in a file with the file extension .py:
# Save this code in a file named mymodule.py
'''
def greeting(name):
  print("Hello, " + name)
'''

# ---------------------------- USE A MODULE --------------------------------
# Now we can use the module we just created, by using the import statement:
'''
import mymodule

mymodule.greeting("Jonathan")
'''

# -------------------------- RE-NAMING A MODULE -----------------------------
# We can create an alias when you import a module, by using the as keyword:
'''
import mymodule as mx

a = mx.person1["age"]
print(a)
'''
# ---------------------------- dir() ---------------------------------------
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
'''
import platform

x = dir(platform)
print(x)
'''
# ----------------------------- Import FROM Module --------------------------
# You can choose to import only parts from a module, by using the from keyword.
'''
from mymodule import person1

print (person1["age"])
'''


########################################### TRY - EXCEPT ######################################
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# --------------------------- EXCEPTION HANDLING -------------------------
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
'''
try:
  print(x)      # the try block will generate an exception since x is not defined 
except:
  print("An exception occurred")
'''

# --------------------------- MANY EXCEPTIONS ----------------------------
'''
try:
  print(x)
except NameError:         # if try block raises NameError then this message is printed
  print("Variable x is not defined")  
except:
  print("Something else went wrong")
'''

# -------------------------- ELSE -----------------------------------------
# You can use the else keyword to define a block of code to be executed if no errors were raised:
'''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
'''

# -------------------------- FINALLY ---------------------------------------
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
'''

# --------------------------- RAISE AN EXCEPTION ----------------------------
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
'''


################################################# USER INPUT ###############################################
# Python 3.6 uses the input() method.
# Python 2.7 uses the raw_input() method.
'''
username = input("Enter username:")
print("Username is: " + username)
'''


################################################ PYTHON STRING FORMATTING #################################
# The format() method allows you to format selected parts of a string.
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
'''
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
'''

# --------------------------- MULTIPLE VALUES -------------------------------
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
'''

# --------------------------- INDEX NUMBERS --------------------------------
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
'''
# ------
'''
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
'''

# --------------------------- NAMED INDEXES --------------------------------
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
'''


################################################### FILE HANDLING ###########################################

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:---
#
#    > "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#    > "a" - Append - Opens a file for appending, creates the file if it does not exist
#    > "w" - Write - Opens a file for writing, creates the file if it does not exist
#    > "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode : --
#
#    > "t" - Text - Default value. Text mode
#    > "b" - Binary - Binary mode (e.g. images)

'''
f = open("demofile.txt", "rt")
'''

# ------------------------------- OPEN FILES -------------------------------
# first open a file using - open() method
# then use read() to read the files content
'''
f = open("demofile.txt", "r")
print(f.read())
'''

# ------------------------------- READING PARTS OF FILES -------------------
# reading a given number of characters from a file.
'''
f = open("demofile.txt", "r")
print(f.read(5))     # first five characters
'''

# ------------------------------ READ LINES --------------------------------
'''
f = open("demofile.txt", "r")
print(f.readline())
'''

# ----------------------------- READ DIFFERENT LINES -----------------------
'''
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
'''

# ----------------------------- READING FILE LINE BY LINE -----------------
# Loop through the file line by line
'''
f = open("demofile.txt", "r")
for x in f:
  print(x)
'''

# ---------------------------- CLOSE FILES --------------------------------
# It is a good practice to always close the file when you are done with it.
'''
f = open("demofile.txt", "r")
print(f.readline())
f.close()
'''


# --------------------------- WRITING TO AN EXISTING FILE ------------------
# To write to an existing file, you must add a parameter to the open() function:
#    > "a" - Append - will append to the end of the file
#    > "w" - Write - will overwrite any existing content
#    > "x" - Create - will create a file, returns an error if the file exist
'''
f = open("demofile2.txt", "a")     # appending to the end of the file
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
'''

# --------------------------- OVERWRITING THE CONTENT -----------------------
'''
f = open("demofile3.txt", "w")     # overwriting the file
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
'''

# --------------------------- DELETING A FILE ------------------------------
# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
'''
import os
os.remove("demofile.txt")
'''

# -------------------------- CHECK IF FILE EXIST THEN DELETE ---------------
# To avoid getting an error, you might want to check if the file exists before you try to delete it
'''
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
'''

# -------------------------- DELETE FOLDER ----------------------------------
# To delete an entire folder, use the os.rmdir() method
'''
import os
os.rmdir("myfolder")
'''







exit()
