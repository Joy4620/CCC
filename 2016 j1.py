W = sum([1 for _ in range(6) if input() == 'W'])
if W == 5 or W == 6:
    print(1)
elif W == 3 or W == 4:
    print(2)
elif W == 1 or W == 2:
    print(3)
else:
    print(-1)
