def shapeE():
    for rows in range(7):
        for cols in range(7): 
            if cols == 0 or rows in {0, 3, 6}:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeE()
