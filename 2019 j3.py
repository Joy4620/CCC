output = []
for i in range(int(input())):
    dump = ''
    string = input() + ' '
    for j in range(len(string)):
        if j == 0:
            previous = string[j], j
            pass
        if string[j] != previous[0]:
            dump += f'{string.count(previous[0], previous[1], j)} {previous[0]} '
            previous = string[j], j
    output.append(dump)

[print(i) for i in output]
