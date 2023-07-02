def calculator(a, b, c, operation1, operation2):
    if operation1 == '+':
        result = a + b
    elif operation1 == '-':
        result = a - b
    elif operation1 == '*':
        result = a * b
    elif operation1 == '/':
        result = a / b
    else:
        print("Invalid operation!")
        return None

    if operation2 == '+':
        result += c
    elif operation2 == '-':
        result -= c
    elif operation2 == '*':
        result *= c
    elif operation2 == '/':
        result /= c
    else:
        print("Invalid operation!")
        return None
    
    return result

# Prompts for entering number and operation:
number1 = float(input("Enter the first number: "))
operation1 = input("Enter the operation (+, -, *, /): ")
number2 = float(input("Enter the second number: "))
operation2 = input("Enter the operation (+, -, *, /): ")
number3 = float(input("Enter the third number: "))

answer = calculator(number1, number2, number3, operation1, operation2)

if answer is not None:
    print("Result:", answer)
