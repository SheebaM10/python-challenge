def shapeJ():
    for rows in range(7):
        for cols in range(7): 
            if (rows == 0):  
                print("*", end="")
            elif (cols == 3) and (rows < 6):  
                print("*", end="")
            elif (rows == 6) and (cols in {1, 2, 3}):  
                print("*", end="")
            elif (rows == 5) and (cols == 0):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeJ()
