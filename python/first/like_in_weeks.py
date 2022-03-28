age = input("How old are you ? ")
year = 90
# Tinh so nam con lai
years_remaining = year - int(age)
months_remaining = years_remaining * 12
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52

#print("You have " + str(days_remaining) + " days and " + str(months_remaining) + " months remaining.")
message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left. (*_*)"
print(message)

