def shapeH():
    for rows in range(7):
        for cols in range(7): 
            if cols in {0, 6}:  
                print("*", end="")
            elif rows == 3:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeH()
