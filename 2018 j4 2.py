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

correct_corner = min(table[0][0], table[0][-1], table[-1][0], table[-1][-1])

while correct_corner is not table[0][0]:
    correct_corner = min(table[0][0], table[0][-1], table[-1][0], table[-1][-1])
    table = list(zip(*table[::-1]))
else:
    for i in table: print(*i)

