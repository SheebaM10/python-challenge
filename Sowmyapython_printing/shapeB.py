def shapeB():
    for rows in range(7):
        for cols in range(7): 
            if rows % 3 == 0 and cols in {0, 1, 2, 3, 4, 5}:  
                print("*", end="")
            elif rows % 3 != 0 and cols in {0, 6}: 
                print("*", end="")
            elif rows == 3:
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeB()
