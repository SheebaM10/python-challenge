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
