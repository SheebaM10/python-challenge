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

def shapeE():
    for rows in range(7):
        for cols in range(7): 
            if cols == 0 or rows in {0, 3, 6}:  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeE()

def shapeF():
    for rows in range(7):
        for cols in range(7): 
            if cols == 0 or (rows == 0 and cols < 6) or (rows == 3 and cols < 5):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeF()

def shapeG():
    for rows in range(7):
        for cols in range(7): 
            if (rows in {0,6}) and (cols in {1,2,3,4,5}):  
                print("*", end="")
            elif (rows in {1,4,5}) and (cols in {0,6}):  
                print("*", end="")
            elif (rows == 2) and (cols == 0):  
                print("*", end="")
            elif (rows == 3) and (cols != 1):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeG()

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

def shapeK():
    for rows in range(7):
        for cols in range(7): 
            if (cols == 0 or rows == cols + 2 or rows + cols == 4):  
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeK()

def shapeL():
    for rows in range(7):
        for cols in range(7):
            if cols == 0 or rows == 6:  # Left vertical line and bottom horizontal line
                print("*", end="")
            else:
                print(" ", end="")
        print()

shapeL()

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

def NShape():
    for row in range(7):
        for col in range(7):
            if row in {0, 6} and col in {0, 6}:
                print('*', end=' ')
            elif row == 1 and col in {0, 1, 6}:
                print('*', end=' ')
            elif row == 2 and col in {0, 2, 6}:
                print('*', end=' ')
            elif row == 3 and col in {0, 3, 6}:
                print('*', end=' ')
            elif row == 4 and col in {0, 4, 6}:
                print('*', end=' ')
            elif row == 5 and col in {0, 5, 6}:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

NShape()

def OShape():
    for row in range(7):
        for col in range(7):
            if row in {0, 6} and col not in {0, 6}:
                print('*', end=' ')
            elif col in {0, 6} and row not in {0, 6}:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

OShape()

def PShape():
    for row in range(7):
        for col in range(7):
            if col == 0 or (row == 0 and col < 6):  
                print('*', end=' ')
            elif row == 3 and col < 6:  
                print('*', end=' ')
            elif col == 6 and row in {1, 2}:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

PShape()

def QShape():
    for row in range(7):
        for col in range(7):
            if (row in {0, 6} and col not in {0, 6}) or (col in {0, 6} and row not in {0, 6}):
                print('*', end=' ')
            elif row == 5 and col == 4:
                print('*', end=' ')
            elif row == 6 and col == 5:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

QShape()

def RShape():
    for row in range(7):
        for col in range(7):
            if col == 0 or (row == 0 and col < 6):  
                print('*', end=' ')
            elif row == 3 and col < 6:  
                print('*', end=' ')
            elif col == 6 and row in {1, 2}:  
                print('*', end=' ')
            elif row > 3 and row - col == 0:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

RShape()


def SShape():
    for row in range(7):
        for col in range(7):
            if row in {0, 3, 6} and col not in {0, 6}:  
                print('*', end=' ')
            elif col == 0 and row in {1, 2}:  
                print('*', end=' ')
            elif col == 6 and row in {4, 5}:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

SShape()

def TShape():
    for row in range(7):
        for col in range(7):
            if row == 0:  
                print('*', end=' ')
            elif col == 3:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

TShape()

def UShape():
    for row in range(7):
        for col in range(7):
            if (col in {0, 6} and row < 6):  
                print('*', end=' ')
            elif row == 6 and col not in {0, 6}:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

UShape()

def VShape():
    for row in range(7):
        for col in range(7):
            if col == 0 and row < 4:  
                print('*', end=' ')
            elif col == 6 and row < 4: 
                print('*', end=' ')
            elif row == 6 and col in {3}:  
                print('*', end=' ')
            elif row == 5 and col in {2, 4}:  
                print('*', end=' ')
            elif row == 4 and col in {1, 5}:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

VShape()

def WShape():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6:  
                print('*', end=' ')
            elif row == 5 and col in {1, 5}:  
                print('*', end=' ')
            elif row == 4 and col in {2, 4}:  
                print('*', end=' ')
            elif row == 3 and col == 3:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

WShape()

def XShape():
    for row in range(7):
        for col in range(7):
            if row == col:  
                print('*', end=' ')
            elif row + col == 6:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

XShape()

def YShape():
    for row in range(7):
        for col in range(7):
            if row <= 3 and (row == col or row + col == 6):  
                print('*', end=' ')
            elif row > 3 and col == 3:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

YShape()

def ZShape():
    for row in range(7):
        for col in range(7):
            if row == 0 or row == 6:  
                print('*', end=' ')
            elif row + col == 6:  
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

ZShape()
