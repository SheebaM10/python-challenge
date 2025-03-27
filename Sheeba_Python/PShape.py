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
