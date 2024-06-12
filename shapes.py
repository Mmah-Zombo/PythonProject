while True:
    # Get the shape the user wants to draw
    print('''Select the shape you want to draw. Shapes:
    T. Triangle, S. Square , K. Kite , R. Rectangle , PL. Parallelogram''')

    shape = input('Enter t, s, k, r, p or pl to select a shape. To quit enter q: ')

    # Checks if drawing should continue
    if shape.lower() == "q":
        print("Thanks for drawing! Bye!")
        break

    size = int(input("Enter the size of the shape: "))

    # Create shapes
    if shape.lower() == "t":  # creates a triangle
        for each in range(size + 1):
            print("*\t" * each)

        print("\n")

        for each in range(0, size):
            print("*\t" * (size - each))

    elif shape.lower() == "s":  # creates a square
        for each in range(size):
            print("*\t" * size)

    elif shape.lower() == "k":  # creates a kite
        for each in range(0, size):
            print(f"{"\t" * (size - each)}{"*\t" * ((each * 2) - 1)}")
        for each in range(0, size):
            print(f"{"\t" * each}{"*\t" * (((size - each) * 2) - 1)}")

    elif shape.lower() == "r":  # creates a rectangle
        for each in range(size):
            print("*\t" * (size + 2))

    elif shape.lower() == "pl":  # creates a parallelogram
        for each in range(0, size):
            print(f"{"\t" * each}{"*\t" * ((size * 2) - 1)}")

    elif shape.lower() == "d":  # creates a diamond
        for each in range(0, size):
            if each > 2:
                print(f"{"\t" * ((size - each) * 2)}{"*\t" * (each * 4)}")
        for each in range(0, size):
            print(f"{"\t" * (each * 2)}{"*\t" * ((size - each) * 4)}")

    print("")
