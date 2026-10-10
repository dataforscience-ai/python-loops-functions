balance=float(input("Enter your account balance: "))
withdrawal=float(input("Enter the amount to withdraw: "))
if withdrawal <= balance:
    balance = balance - withdrawal
    print("Withdrawal successful. Your new balance is:", balance)
    print("Remaining balance:", balance)
else:
    print("Insufficient funds")
