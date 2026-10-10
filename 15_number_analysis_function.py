def analyze_number(number):

    result = {}

    # Positive / Negative / Zero
    if number > 0:
        result["Type"] = "Positive"

    elif number < 0:
        result["Type"] = "Negative"

    else:
        result["Type"] = "Zero"

    # Even / Odd
    if number % 2 == 0:
        result["Parity"] = "Even"
    else:
        result["Parity"] = "Odd"

    # Prime / Not Prime
    is_prime = True

    if number <= 1:
        is_prime = False

    else:
        for i in range(2, number):

            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        result["Prime"] = "Prime"
    else:
        result["Prime"] = "Not Prime"

    return result


number = int(input("Enter a number: "))

analysis = analyze_number(number)

print(analysis)