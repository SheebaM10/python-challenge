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
