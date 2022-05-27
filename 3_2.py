def data(first_name, last_name, year_of_birth, city_of_residence, email, phone):
    print(f"Your first name is {first_name}.,"
          f" Your last name is {last_name}., "
          f"You were born in {year_of_birth}., "
          f"Do you live in {city_of_residence}., "
          f"Your email address is {email}., "
          f"Your phone number is {phone}.")


first_name = input("Enter your first name: ")
last_name = input("Enter your first name: ")
year_of_birth = input("Enter the year of your birth: ")
city_of_residence = input("Enter your city of residence: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
data(first_name, last_name, year_of_birth, city_of_residence, email, phone)
