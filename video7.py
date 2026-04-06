# This Video :

# More about for Loops

a = ["apple", "Orange", "Watermelon"]

for element in a:
    print(element)

for i in range(0, 3):
    print(i)



for i in range(len(a)):
    print(a[i])



for i in range(len(a)):
    for j in range(i + 1):
    # i = 0 => j = 0
    # i = 1 => j = 0,
        print(a[i])



print(list(range(1, 30)))

total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i 
    elif i % 5 == 0:
        total += i
print (total)



total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)




given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total = 0
for i in given_list:
    if i < 0 :
        total += i
print(total)



given_list2 = [2, 4, 5, 1, 3, 7, 6, 8, 9, -9, -5, -8, -7, -6, -5, -4, -3, -2, -1]
total2 = 0
j = len(given_list2) - 1
while given_list2[j] < 0:
    total2 += given_list2 [j]
    j -= 1
print(total2)




