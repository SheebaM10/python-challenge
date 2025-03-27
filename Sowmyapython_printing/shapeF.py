def shapeF():
    for rows in range(7):
        for cols in range(7): 
            if cols == 0 or (rows == 0 and cols < 6) or (rows == 3 and cols < 5):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeF()
