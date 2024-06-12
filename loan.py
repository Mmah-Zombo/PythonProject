# Get salary from the user
annual_salary = float(input("How much do you earn annually in your current company? "))
years_worked = int(input("How many years have you worked for in your current company? "))

if annual_salary >= 30_000 and years_worked >= 2:
    print("You are eligible for the loan!")
else:
    print("Sorry. You are not eligible for the loan.")
