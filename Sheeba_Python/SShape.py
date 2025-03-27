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
