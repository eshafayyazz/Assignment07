# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Input numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# Call the function and display the result
result = add_numbers(number1, number2)
print("The sum of {} and {} is {}".format(number1, number2, result))
