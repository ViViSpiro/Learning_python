n = int(input("Enter a positive integer: "))
max = 0
while n > 0:
    m = n % 10
    if m > max:
        max = m
        if max == 9:
            break
    n = n // 10
print("Maximum digit in a number is ", max)
