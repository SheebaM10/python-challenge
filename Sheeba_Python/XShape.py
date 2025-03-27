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
