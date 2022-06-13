def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return int(num1 / num2)
        except ZeroDivisionError:
            return "Can't divide by 0!"
