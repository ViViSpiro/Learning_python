seasons = {"spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11], "winter": [12, 1, 2]}
month = int(input("Enter the month: "))
for key in seasons.keys():
    if month in seasons[key]:
        print("It's ", key)
