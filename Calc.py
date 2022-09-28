## write a perfect calculator
print("Welcome to the calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
print("7. Floor Division")
print("8. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is: ", num1 + num2)
elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The difference is: ", num1 - num2)
elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The product is: ", num1 * num2)
elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The quotient is: ", num1 / num2)
elif choice == 5:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The remainder is: ", num1 % num2)
elif choice == 6:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The result is: ", num1 ** num2)
elif choice == 7:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The result is: ", num1 // num2)
elif choice == 8:
    exit()
    ## End of the program