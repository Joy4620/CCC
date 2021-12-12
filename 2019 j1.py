output = []
for i in range(2):
    three = int(input())*3
    two = int(input())*2
    one = int(input())
    output.append(one+two+three)

if output[0] == output[1]:
    print('T')
elif output[0] > output[1]:
    print('A')
else:
    print('B')
