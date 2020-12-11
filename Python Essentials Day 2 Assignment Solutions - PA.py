#!/usr/bin/env python
# coding: utf-8

# # Solution 1 - Try 5 Different functions of the String in Python.

# In[13]:


#upper() - Converts a string into upper case

Verification_Code = "Pri10yA25."
Verification_Code.upper()


# In[14]:


#isalpha() - Returns True if all characters in the string are in the alphabet

Verification_Code = "Pri10yA25."
Verification_Code.isalpha()


# In[141]:


#strip() - Returns a trimmed version of the string ; rstrip() - Returns a right trim version of the string ; lstrip() - Returns a left trim version of the string
#isalnum() - Returns True if all characters in the string are alphanumeric

Verification_Code = "Pri10yA25."
No_SpecialChar = Verification_Code.strip(".")
No_SpecialChar.isalnum()


# In[19]:


#swapcase() - Swaps cases, lower case becomes upper case and vice versa

Verification_Code = "Pri10yA25."
Verification_Code.swapcase()


# In[28]:


#find() - Searches the string for a specified value and returns the position of where it was found

Verification_Code = "Pri10yA25."
Verification_Code.find("A")


# # Solution 2 - Try 5 Different functions of the List object in Python

# In[140]:


#Joining/Concatenating List can be done using + operator, exaple New_List = List1 + List2
# extend() - Adds elements from one list to another list
# append - Adds an element at the end of the list

Christmas_List = ["Christmas Tree", 25, ["Withdraw from bank", 5000], "Plum Cake"]
NewYears_List = ["Decorations", 31, "Fire Crackers"]

Christmas_List.extend(NewYears_List)

Christmas_List.append("TravelBags")

Vacation_List = Christmas_List + ["Flight and Hotel Booking"]

print(Vacation_List)


# In[42]:


#pop() - Removes the element at the specified position

Christmas_List = ["Christmas Tree", 25, ["Withdraw from bank", 5000], "Plum Cake"]
NewYears_List = ["Decorations", 31, "Fire Crackers"]
Christmas_List.pop(2)
print(Christmas_List)


# In[40]:


#remove() - Removes the item with the specified value

Christmas_List = ["Christmas Tree", 25, ["Withdraw from bank", 5000], "Plum Cake"]
NewYears_List = ["Decorations", 31, "Fire Crackers"]
Christmas_List.remove(25)
print(Christmas_List)


# In[49]:


#insert() - Adds an element at the specified position

Vacation_List = ['Christmas Tree', 25, ['Withdraw from bank', 5000], 'Plum Cake', 'Decorations', 31, 'Fire Crackers']
Vacation_List.insert(-2, ["Deposit in bank", 10000])
print(Vacation_List)


# In[52]:


#clear() - Removes all the elements from the list

Vacation_List = ['Christmas Tree', 25, ['Withdraw from bank', 5000], 'Plum Cake', 'Decorations', ['Deposit in bank', 10000], 31, 'Fire Crackers']
New_Festive_List = Vacation_List.clear()
print(New_Festive_List)


# # Solution 3 - Experiment with at least 5 default functions of Dictionary.

# In[74]:


#items() - Returns a list containing a tuple for each key value pair

LUStudent1 = {"ID":"LU1025", "Name":"Priyanka Awatramani", "Age":20}
LUStudent1.items()


# In[72]:


#update() - Removes the last inserted key-value pair

LUStudent1 = {"ID":"LU1025", "Name":"Priyanka Awatramani", "Age":20}
LUStudent1.update({"Age":21})
print(LUStudent1)


# In[70]:


#popitem() - Removes the last inserted key-value pair

LUStudent1 = {'ID': 'LU1025', 'Name': 'Priyanka Awatramani', 'Age': 21, "Course":"Python Essentials"}
LUStudent1.popitem()
print(LUStudent1)


# In[85]:


#setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

LUStudent1 = {'ID': 'LU1025', 'Name': 'Priyanka Awatramani', 'Age': 21, "Course":"Python Essentials"}
LU_ID = LUStudent1.setdefault("NewJoinerLUCoins","10 New Joiner Coins")
print(LU_ID)


# In[86]:


#keys() - Returns a list containing the dictionary's keys

LUStudent1 = {'ID': 'LU1025', 'Name': 'Priyanka Awatramani', 'Age': 21, "Course":"Python Essentials"}
LUStudent1.keys()


# In[142]:


#values() - Returns a list of all the values in the dictionary

LUStudent1 = {'ID': 'LU1025', 'Name': 'Priyanka Awatramani', 'Age': 21, "Course":"Python Essentials"}
LUStudent1.values()

