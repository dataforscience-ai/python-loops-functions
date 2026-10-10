n=int(input("Enter a number: "))
total=0
for i in range(1, n + 1):
    total += i  
average = total / n if n > 0 else 0
print("Sum:", total)
print("Average:", average)