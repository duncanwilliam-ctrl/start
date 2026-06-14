def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("operator: ")

    if operator.lower() == 'q' or num1 == 0 or num2 == 0:
        print('goodbye, \nhope to see you agein')
        break

    elif operator == '+':
        result = add(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    else:
        if num2 != '0':
            result = divide(num1, num2)
        else:
            result = 0
            print('error-divide by zero. Not good my friend.')

    print(
        f" num1 is :{num1} , num2 is :{num2}, and \n the result is :{result}")
