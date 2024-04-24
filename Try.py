# print("Hello world")
# print("My name is " + "Peanut")
# print("My age is " + "17")
# print("My age is " + str(17))
# username = input("Enter your name: ")
# print("Hello " + username)
# age = input("Enter your age: ")
# print("My age is " + str(age))
# age = int(input("Enter your age: "))
# print("in 2025, you will be " + str(age + 1))

# print("Welcome to the Cloud chaser ride!")
# height = int(input("What is your height in cm? : "))

# if height >= 120:
#     print("Enjoy the ride! :)")

# else:
#     print("Well you are not tall enough come back next time >_<")

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
