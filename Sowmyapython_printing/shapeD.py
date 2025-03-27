def shapeD():
    for rows in range(7):
        for cols in range(7): 
            if cols == 0:  
                print("*", end="")
            elif cols == 6 and rows not in {0, 6}: 
                print("*", end="")
            elif rows in {0, 6} and cols in {1, 2, 3, 4, 5}:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeD()
