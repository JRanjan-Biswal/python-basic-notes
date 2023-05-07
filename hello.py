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
print("free" in txt)  # "in" is used to check a substring in string 
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
print(a + " " + BrokenPipeError)
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

# IMPORTANT: LIST constructor can be used to creare a list
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
print(thislist)
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
print(set3)    # {1, 2, 3, 'b', 'c', 'a'}
'''


# update() : method that inserts all the items from one set into another
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)    # {1, 2, 3, 'b', 'c', 'a'}
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
#A will not overwrite a 
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
  print("Python is " + x)

myfunc()

print("Python is " + x) 
'''

# The global Keyword
# If you use the global keyword, the variable belongs to the global scope
'''
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
'''


exit()
