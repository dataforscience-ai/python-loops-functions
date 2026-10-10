while True:

    print("\nCalculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting Calculator...")
        break

    elif choice not in [1, 2, 3, 4, 5]:
        print("Invalid Choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:

        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero is not allowed")

    elif choice == 5:

        if num2 != 0:
            print("Result =", num1 % num2)
        else:
            print("Modulus by zero is not allowed")
            