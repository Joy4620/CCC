one, two, three, four = [int(input()) for _ in range(4)]
if one == 8 or one == 9:
    if two == three:
        if four == 8 or four == 9:
            print('ignore')
            quit()
print('answer')
