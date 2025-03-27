def shapeM():
    for rows in range(7): 
        for cols in range(7):  
            if cols == 0 or cols == 6: 
                print("*", end="")
            elif rows == cols and cols <= 3:  
                print("*", end="")
            elif (rows + cols == 6) and (cols >= 3):  
                print("*", end="")
            else:
                print(" ", end="")  
        print()  

shapeM()
