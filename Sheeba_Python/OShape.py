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
