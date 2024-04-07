result = 0  # Initialize result outside the loop

while True:
    num = float(input("Enter your number: "))

    operation = input("Enter your operator (+, -, *, /) or '=' to finish: ")

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
    elif operation == "=":
        break
    else:
        print("Invalid input")

print("Final result:", result)
