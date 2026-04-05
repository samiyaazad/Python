#This Video :
# While Loops & The Break Statement


total = 0
for i in range(1, 5):
    total += i 
print(total)



# this in while : 
total2 = 0 
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)



given_list = [10, 9, 8, 7, 6, 5, 4, -4, -5, -6, -7, -8, -9, -10]

total3 = 0
k = 0
while given_list[k] > 0:
    total3 += given_list[k]
    k += 1
print(total3)


# if there is no negative
list_given = [10, 9, 8, 7, 6, 5, 4]

total4 = 0
m = 0
while m < len(list_given) and list_given[m] > 0:
    total4 += list_given[m]
    m += 1
print(list_given)
print(total4)



# in FOR Loop 
list_given2 = [10, 9, 8, 7, 6, 5, 4, -4, -5, -6, -7, -8, -9, -10]

total5 = 0
for element in list_given2:
    if element <= 0:
        break
    total5 += element
print(element)



