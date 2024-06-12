# Get the weight and year from the user
weight = int(input("Enter the automobile's weight: "))
year = int(input("Enter the automobile's model year: "))

# Set the initial value of the weight class and registration fees
weight_class = 0.0
registration_fees = 0.0

# Check the automobile's model year value
if year <= 1990:
    if weight < 2700:  # Check the weight of the automobile
        weight_class = 1
        registration_fees = 26.50
    elif 2700 <= weight <= 3800:
        weight_class = 2
        registration_fees = 35.50
    else:
        weight_class = 3
        registration_fees = 56.50

elif 1991 <= year <= 1999:
    if weight < 2700:
        weight_class = 4
        registration_fees = 35.00
    elif 2700 <= weight <= 3800:
        weight_class = 5
        registration_fees = 45.50
    else:
        weight_class = 6
        registration_fees = 62.50

elif year >= 2000:
    if weight < 3500:
        weight_class = 7
        registration_fees = 49.50
    else:
        weight_class = 8
        registration_fees = 45.50

print(f'The automobile\'s weight class and registration fees are {weight_class} and {registration_fees} respectively')
