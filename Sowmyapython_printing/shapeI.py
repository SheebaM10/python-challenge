def shapeI():
    for rows in range(7):
        for cols in range(7): 
            if rows in {0, 6}: 
                print("*", end="")
            elif cols == 3:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeI()
