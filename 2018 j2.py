spaces = int(input())
park1 = input()
park2 = input()

count = 0
for i in range(spaces):
    if park1[i] == 'C' and park2[i] == 'C':
        count += 1
print(count)
