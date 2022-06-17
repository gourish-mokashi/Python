# Dictionary is nothing but set of values
d1 = {}
print(type(d1))
# here we use {} Parenthesis bracket to make a dictionary from variable
# and we must use type() function tell the type of function

d2 = {"Python": "For ML and AI development", "Java": "For application development",
      "Javascript": "For web Development"}

print(d2["Python"])
# The above is an example of Dictionary datatype
d3 = {"Ai dev": "Python", "Web dev": "Javascript"
    , "App dev": {"Frontend": "XML", "backend": "Java, dart", "database": "Mysql"}
      }
print(d3["App dev"])
# here in dict wwe can create sub-dict to
# If i want to add something extra then i will
d3["blockchain dev"] = "Solidity"
print(d3)
# Add
# what if i want to delete some thing
del d3["blockchain dev"]
print(d3)
# Deleted

print(d3.copy())
# Here .copy() Function make a copy of particular dict

# d4 = d3
# del d4["Ai dev"]
# print(d3)
# NOTE: The above 3 lines are commented to avoid error u need to assume uncommented
# here d4 is exactly referring to d3 if we modify d4 then d3 also will change

# To Avoid such duplicating error we must use .copy() function
d5 = d3.copy()
del d5["Ai dev"]
print(d3)
# Here d5 and d3 are not exactly referring to each other

d3.update({'Game Dev': "C#"})
print(d3)
# here .update add set to dict

print(d3.keys())
# here .Keys() Shows the key words in the dict

print(d3.items())
# here .items() shows all the items from the dict
