# This Video : 

# List in Python 

a = [3, 10, -1] #to define list 
print(a)

a.append(1) # add to list
print(a)

a.append("hello") # same to add in list
print(a)

b= [10, 11] 
a.append(b)
print(a)

a.pop() #to remove from list 
print(a)

a.pop()
print(a)

print(a[0]) # to retrive one specific item

print(a[3])

a[0] = 100 # to change a specific item 
print(a)


#Problem : Swepping 

#way-1
b = ["banana", "apple", "Microsoft"] # showing them in different order

fail = b[0]
b[0] = b[2]
b[2] = fail

print(b)


#way-2
c = ["eggs", "oil", "apple"]

c[0], c[1], c[2] = c[1], c[2], c[0]

print(c)