# This video :

# Dictionaries in Python ==> a look-up table

d = {} # this define a empty dictionary  || this also can be written as d = dict()
d ["George"] = 24 
d ["Tom"] = 36 # keys are commonly strings or numbers
d ["Jenny"] = 16 # Strings are specific and can't be changed but the numbers part can be 

print(d["George"])
print(d["Tom"])
print(d["Jenny"])




# how to iterate over key-value pairs :
for key, value in d.items ():
    print("") # for a space 
    print("key")
    print(key)
    print("value")
    print(value) 
    print("")