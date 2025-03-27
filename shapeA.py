def shapeA():
    for rows in range(7):
        for cols in range(5):
            if(rows==0) and (cols in {1,2,3}):
                print("*", end="")
            elif (rows in {1,2,3,5,6})and (cols in{0,4}):
                print("*", end="")
            elif(rows==3):
                print("*", end="")
            else:

                print(" ",end="")
        print()

shapeA()


