#!/usr/bin/env python3


def admin_login(username, password):
    # USING TERNARY TO DETERMINE IF username and password match VALUES
    results = (
        "Access granted"
        if username.lower() == "admin" and password == "12345"
        else "Access denied"
    )
    return results


def hows_the_weather(temperature):
    if int(temperature) < 40:
        return "It's brisk out there!"

    # elif int(65 <= temperature > 40):
    elif int(temperature > 40) and int(temperature <= 65):
        return "It's a little chilly out there!"

    elif int(temperature > 85):
        return "It's too dang hot out there!"

    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if int(num % 3 == 0) and int(num % 5 == 0):
        return "FizzBuzz"

    elif int(num % 5) == 0:
        return "Buzz"

    elif int(num % 3) == 0:
        return "Fizz"

    else:
        return num


def calculator(operation, num1, num2):
    if operation == "/":
        return num1 / num2

    elif operation == "+":
        return num1 + num2

    elif operation == "*":
        return num1 * num2

    elif operation == "-":
        return num1 - num2

    else:
        print("Invalid operation!\n")
        return None
