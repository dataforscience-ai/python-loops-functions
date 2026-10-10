def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
result = my_sum(numbers)
print("The sum is:", result)