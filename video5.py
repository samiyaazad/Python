# This Video :
#     Loops

a = ["banana", "apple", "microsoft"]

for element in a: 
    print(element) 
    print(element) # show 2 times





b = [20, 30, 10]

for e in b:
    print(e)




c = [20, 10, 0]
total = 0
for  e in c:
    total = total + e
print(total)




#Problem
d= [50, 50, 50]
total = 0
for e in d:
    total = total + e
print(total)



#way-1
c = list(range(1, 20))
print(c)


#way-2
for i in range(1, 9):
    print(i)




#SUM
total12 = 0
for i in range(1, 5):
    total12 += i
print(total12)



print(list(range(1,8)))


total13 = 0
for i in range(1, 8):
    if i % 3 == 0:
       total13 += i
print(total13)




total14 = 0
for i in range(1, 100):
    if i % 3 == 0 & i % 5 == 0:
        total14 = total14 + i 
print(total14)
