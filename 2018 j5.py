'''
Sample Input 1
3
2 2 3
0
0
Output for Sample Input 1
Y
2


Sample Input 2
3
2 2 3
0
1 1
Output for Sample Input 2
Y
2
'''

rules = [[1, 2, 3], 
         [3, 1],
         [2, 1, 4],
         [0]]

class Point():
    def __init__(self, x, parent=None):
        self.x = x
        self.step = 0
        self.record=[x]
        if parent:
            self.step = parent.step
            self.record=parent.record+self.record


Stack = [Point(1)]
visited = set()
steps = set()

while Stack:
    P = Stack.pop()

    if P.x in visited:
        print(visited, 'visited')
        continue

    if len(visited) == len(rules):
        for i in range(len(rules)):
            if i+1 not in visited:
                print('N')
                break
        print('Y')
        break

    visited.add(P.x)
    P.step += 1

    if rules[(P.x)-1][0] == 0:
        steps.add(P.step)
        P.step = 0
        continue

    print(len(rules[P.x]))
    for i in range(len(rules[(P.x)])):
        Stack.append(Point(rules[(P.x)-1][i], P))
        print(rules[(P.x)-1][i], 't')

print(P.step, 'p.step')
print(P.record, 'p.record')
print(visited, 'visited')
print(steps)
