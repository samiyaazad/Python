# This Video :

            # What are functions?
            # Creating a BMI Calculator



# a collection of instructions
# a collection of code


def function1():
    print("ahhhhh")
    print("ahhhhh2")
function1() #to show the function
print("this is outside of the function")





# a mapping 
# input or an argument

def function2 (x):
    return 2*x

#type-1
a = function2(3) # return value or output 
print(a)

b = function2(4)
print(b)

c = function2(5)
print(c)


#type-2
def function3(x, y):
    return x + y
e = function3(5, 6)
print(e)


#combinding type-1 & type-2
def function4(z):
    print(z) # output : x
    print("still in this function")
    return 3*z
f = function4(4) 
print(f) # outout : 12


#type-3
def function5(some_value):
    print(some_value) # output: 4
    print("weee") # output: weee

function5(4)





#Problem 1 : BMI calculator 
name1 = "DQ"
height1 = 2 
weight1 = 90

name2 = "IS"
height2 = 1.8
weight2 = 70

name3 = "YK"
height3 = 2.5
weight3 = 160

def bmi_(name, height, weight):
    bmi = weight / (height ** 2)
    print("BMI : ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight"
    else: 
        return name + " is overweight"

result1 = bmi_(name1, height1, weight1)
result2 = bmi_(name2, height2, weight2)
result3 = bmi_(name3, height3, weight3)

print(result1)
print(result2)
print(result3)



#Problem 2 : KM = CONVERT(MILES)
# km= 1.6 *miles

name1 = "DQ"
name2 = "IS"
name3 = "YK"

miles1 = 2.7
miles2 = 5.4
miles3 = 10.1

x = 1.6

def converter(name, miles):
    convert = miles * x
    print(convert)
    if miles > 10:
        return name + " is qualified"
    else: 
        return name + " is not qualified."
    
result1 = converter(name1, miles1)
result2 = converter(name2, miles2)
result3 = converter(name3, miles3)

print(result1)
print(result2)
print(result3)





#Problem - 3 : Speed Checker

car1 = "Ferrari"
distance1 = 700
time1 = 2


car2 = "Williams"
distance2 = 100
time2 = 2


car3 = "McLaren"
distance3 = 150
time3 = 2.5


def speed_calculator(car, distance, time):
    speed = distance / time 
    if speed > 60:
        return car + " is speeding"
    else: 
        return car + " is safe"

result1 = speed_calculator(car1, distance1, time1)
result2 = speed_calculator(car1, distance2, time2)
result3 = speed_calculator(car3, distance3, time3)

print(result1)
print(result2)
print(result3)





#Problem - 3 : Circle Area & Size Check 

circle1 = "C1"
radius1 = 3

circle2 = "C2"
radius2 = 4

circle3 = "C3"
radius3 = 2

def circle_area(circle, radius):
    π = 3.14
    area =  π * ( radius ** 2)

    if area > 50:
        return circle + " is large circle" 
    else: 
        return circle + " is small circle"

result1 = circle_area(circle1, radius1)
result2 = circle_area(circle2, radius2)
result3 = circle_area(circle3, radius3)

print(result1)
print(result2)
print(result3)





#Problem - 3 : Grade Calculator

student1 = "Ali"
mark1 = 85

student2 = "Sara"
mark2 = 92

student3 = "Zara"
mark3 = 48

def gradeCalculate(student, mark):
    grade = mark
    if  mark >= 90 :
        return student + " got A"
    elif mark >= 75:
        return student + " got B"
    elif mark >= 50:
        return student + " got C"
    else:
        return student + " Failed"

result1 = gradeCalculate(student1, mark1)
result2 = gradeCalculate(student2, mark2)
result3 = gradeCalculate(student3, mark3)

print(result1)
print(result2)
print(result3)