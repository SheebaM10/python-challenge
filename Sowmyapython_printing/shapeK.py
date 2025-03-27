def shapeK():
    for rows in range(7):
        for cols in range(7): 
            if (cols == 0 or rows == cols + 2 or rows + cols == 4):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeK()

