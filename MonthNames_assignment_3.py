
# Exercise 1

months = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

month_number = int(input("Enter the month: "))
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 12.")

# Exercise 2

full_price = 6
age = int(input("Enter your age: "))
if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

# Print the ticket price
print('Your cost is;', ticket_price)

# Exercise 3

weight = int(input("Enter your weight in (kg): "))
height = int(input("Enter your height in (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
elif 25 <= bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obese"


print('Your BMI is;', bmi)
print('You are in the range;', status)

# Exercise 4

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

# To find the greatest number
greatest = max(n1, n2, n3)

# To Print the greatest number
print(f"The greatest number is: {greatest}")

# Exercise 5

number = int(input("Enter a number to find its factorial: "))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i

    # Print the result
    print('The factorial of the given number is;', factorial)

# Exercise 6

num = int(input("Enter a number: "))

# Initialize variables
reversed_num = 0

while num != 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print('The reversed number is;',  reversed_num)

# Exercise 7
# Program to find the multiples of a number using a loop

num = int(input("Enter a number: "))
limit = int(input("Enter the limit up to which you want multiples: "))

for i in range(1, limit + 1):
    multiple = num * i
    print(multiple)

# Exercise 8

user_input = 1
while user_input != 'done':
    user_input = input("Enter a value (or type 'done' to finish): ")
    if user_input != 'done':
        print(user_input)
print("Done")

# Exercise 9

for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Exercise 10

for i in range(5, 0, -1):

    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

