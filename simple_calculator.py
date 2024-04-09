result = float(input("Enter your number: "))

while True:
    operation = input("Enter your operator (+, -, *, /) or '=' to finish: ")

    if operation not in ["+", "-", "*", "/", "="]:
        print("Only operators are allowed.")
        break

    if operation == "=":
        break

    num = float(input("Enter your number: "))

    if operation == "+":
        result += num
    elif operation == "-":
        result -= num
    elif operation == "*":
        result *= num
    elif operation == "/":
        if num == 0:
            print("Zero is not a valid divisor.")
        else:
            result /= num

print("Final result:", result)
