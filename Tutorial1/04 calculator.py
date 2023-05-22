# User input: 2 numbers
# NOTE: default user input is string, we need to convert to a number
# casting to integer, e.g. int("5") = 5
# casting to float, e.g. float("5.5") = 5.5
num_1 = input("Enter the 1st number: ")
num_2 = input("Enter the 2nd number: ")
print("Input numbers are: " + num_1 + " & " + num_2)
sum = float(num_1) + float(num_2)
print(sum)
print("The sum is: " + str(sum))