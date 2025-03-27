def shapeC():
    for rows in range(7):
        for cols in range(7):  
            if rows in {0, 6} and cols in {1, 2, 3, 4, 5}:  
                print("*", end="")
            elif rows in {1, 5} and cols in {0, 6}: 
                print("*", end="")
            elif rows in {2, 3, 4} and cols == 0:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeC()
