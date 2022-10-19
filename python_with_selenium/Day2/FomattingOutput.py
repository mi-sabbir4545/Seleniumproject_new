name,age, sal = "john",30,5000.50

print("Name is: ", name)
print(age)
print(sal)
print(name, age,sal)

print("Name is: %s age is: %d sal is: %g" % (name, age, sal))


print("Name is: {} age is: {} sal is: {}" .format(name, age, sal))

num1 = input("enter number: ")
num2 = input("enter second number: ")

print(float(num1) + float(num2))