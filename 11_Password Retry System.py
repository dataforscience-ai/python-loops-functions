correct_password="python123"
attempt=0
while attempt<3:
    password=input("Enter password: ")
    if password==correct_password:
        print("Access granted.")
        break
    else:
        attempt += 1
        if attempt<3:
            print("Incorrect password. Please try again.")
if attempt==3:
            print("Too many incorrect attempts. Access denied.")