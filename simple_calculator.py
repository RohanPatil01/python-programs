result = float(input("Enter your number: "))

while True:
    operation = input("Enter your operator (+, -, *, /) or '=' to finish: ")
    
    if operation != "=":
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
    elif operation == "=":
        break
    else:
        print("Invalid input")

print("Final result:", result)