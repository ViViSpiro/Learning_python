def sum_f():
    result = 0
    while True:
        nums = input("Enter a list of numbers separated by a space, or q to exit: ").split()
        for i in nums:
            if i == "q":
                print(f"The sum of the entered numbers is equal to {result}. Exit.")
                return result
            else:
                try:
                    result += float(i)
                except ValueError:
                    print("Invalid value! Enter numbers or q.")
            print(f"The sum of the numbers is {result}")


print(sum_f())
