def calculate_salary(name, basic_salary, bonus_percentage, tax_percentage):

    bonus_amount = (basic_salary * bonus_percentage) / 100

    gross_salary = basic_salary + bonus_amount

    tax_amount = (gross_salary * tax_percentage) / 100

    final_salary = gross_salary - tax_amount

    return gross_salary, tax_amount, final_salary


for i in range(5):

    print(f"\nEmployee {i+1}")

    name = input("Enter Employee Name: ")

    basic_salary = float(input("Enter Basic Salary: "))

    bonus_percentage = float(input("Enter Bonus Percentage: "))

    tax_percentage = float(input("Enter Tax Percentage: "))

    gross_salary, tax_amount, final_salary = calculate_salary(
        name,
        basic_salary,
        bonus_percentage,
        tax_percentage
    )

    print("Employee Name:", name)
    print("Gross Salary:", gross_salary)
    print("Tax Amount:", tax_amount)
    print("Final Salary:", final_salary)
    