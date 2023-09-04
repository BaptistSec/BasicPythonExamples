try:
    calc_inp = input("Enter a calculation (e.g., 'num1 + num2'): ")
    num1_str, operation, num2_str = calc_inp.split()
    num1 = int(num1_str)
    num2 = int(num2_str)

    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} plus {num2} is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} minus {num2} is {result}")
    else:
        raise ValueError("Invalid operation. Supported operations are '+' and '-'.")

except ValueError as e:
    print(f"Invalid input: {e}")

# Add a pause to keep the window open
input("Press Enter to exit...")
