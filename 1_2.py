n = int(input("Enter the number of seconds: "))
hours = n // 3600
minutes = (n - hours * 3600) // 60
seconds = n % 60
print(f"{hours:02d} : {minutes:02d} : {seconds:02d}")
