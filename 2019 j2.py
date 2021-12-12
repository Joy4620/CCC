output = []
for i in range(int(input())):
    times, char = input().split()
    output.append(char*(int(times)))

[print(i) for i in output]

