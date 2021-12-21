'''
Sample Input
3 10 12 5

Output for Sample Input
0 3 13 25 30
3 0 10 22 27
13 10 0 12 17
25 22 12 0 5
30 27 17 5 0
'''

a, b, c, d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

print(0, a, a+b, a+b+c, a+b+c+d)
print(a, 0, b, b+c, b+c+d)
print(a+b, b, 0, c, c+d)
print(a+b+c, b+c, c, 0, d)
print(a+b+c+d, b+c+d, c+d, d, 0)


distance = [int(a), int(b), int(c), int(d), 0]

# print(0, distance[0:0], sum(distance[0:2]), sum(distance[0:3]), sum(distance[0:4]))
# print(distance[0:0], 0, sum(distance[1:2]), sum(distance[1:3]), sum(distance[1:4]))


# for i in range(4):
#     for j in range(4):
#         print(0, distance[0:0], sum(distance[0:2]), sum(distance[0:3]), sum(distance[0:4]))

