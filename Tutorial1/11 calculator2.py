# User input: 2 numbers
# NOTE: default user input is string, we need to convert to a number
# casting to integer, e.g. int("5") = 5
# casting to float, e.g. float("5.5") = 5.5
num_1 = float(input("Enter the 1st number: "))
op = input("Enter the operator: ")
num_2 = float(input("Enter the 2nd number: "))

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "/":
    print(num_1 / num_2)
elif op == "*":
    print(num_1 * num_2)
else:
    print("Invalid operator")
