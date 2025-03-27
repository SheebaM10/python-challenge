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
