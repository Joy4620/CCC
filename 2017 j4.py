addtime = int(input())

clock = [1, 2, 0, 0]
count = 0
times = 0

while times != addtime%720:
    if clock[3] == 9:
        clock[3] = 0
        if clock[2] == 5:
            clock[2] = 0
            if clock[0] == 1 and clock[1] == 2:
                clock[0] = 0
                clock[1] = 1
            elif clock[0] == 0 and clock[1] == 9:
                    clock[0] = 1
                    clock[1] = 0
            else:
                clock[1] += 1
        else:
            clock[2] += 1
    else:
        clock[3] += 1

    difference = clock[2]-clock[1]
    if clock[0] != 0:
        if clock[0] + difference == clock[1] and clock[1] + difference == clock[2] and clock[2] + difference == clock[3]:
            count += 1
    else:
        if clock[1] + difference == clock[2] and clock[2] + difference == clock[3]:
            count += 1

    times += 1

print(31*(addtime//720) + count)
