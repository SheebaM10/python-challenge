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
