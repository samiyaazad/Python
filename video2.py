# This Video :

            # If-else statements
            # BMI Calculator






# if statement
a = 1
b = 2 

if a < b:
    print("a is less than b") # In python it need to be 4 spaces for if's statement
    print("Definitely")
print("Not Sure")






# if-else statement
c = 5
d = 4

if c < d:
    print("c is less")
else: 
    print("NO")
print("Outside")






## if-elif-else statement
e = 38
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is not less than f")





##  If else in if else statement
g = 2
h = 8

if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")





##  BMI CALCULATOR statement
name = "Duang"
sex = "male" 
weight = 39
height = 1.75

bmi = weight / (height * height)

print("bmi is ")
print(bmi)

if bmi < 18.5:
    print(name)
    print("Duang is UNDERWEIGHT")
elif 18.6 < bmi < 24.9:
    print(name)
    print("Duang is HEALTHY WEIGHT")
elif 25.0 < bmi < 29.9:
    print(name)
    print("Duang is OVERWEIGHT")
else:
    print(name)
    print("Duang is OBESE")
