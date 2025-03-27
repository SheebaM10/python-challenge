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
