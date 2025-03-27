def shapeL():
    for rows in range(7):
        for cols in range(7):
            if cols == 0 or rows == 6:  # Left vertical line and bottom horizontal line
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeL()
