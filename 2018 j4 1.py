'''
Sample Input 1
2
1 3
2 9
Output for Sample Input 1
1 3
2 9

Sample Input 3
3
3 7 9
2 5 6
1 3 4
Output for Sample Input 3
1 2 3
3 5 7
4 6 9
'''

plants = int(input())
table = [list(map(int, input().split())) for _ in range(plants)]

for i in range(3):
    ordered = True

    for j in range(plants):
        if tuple(table[j]) != tuple(sorted(table[j])):
            ordered = False

    plant_order = []
    for j in range(plants):
        plant_order.append(table[j][0])
    if plant_order != sorted(plant_order):
        ordered = False

    if ordered:
        for k in table: print(*k)
        quit()
    table = list(zip(*table[::-1]))

