book = [[1, 3, 2], 
        [3, 2],
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
    if P.x in visited:  # this line isn't right
        continue

    visited.add(P.x)
    P.step += 1

    if book[(P.x)-1][0] == 0:
        steps.add(P.step)
        P.step = 0
        continue
    for i in range(len(book[P.x-1])):
        Stack.append(Point(book[P.x-1][i], P))

answer = 'N'
if len(visited) == len(book):
    answer = 'Y'

print('steps set is', steps)
print('recorded path is', P.record)
print('we visited these pages:', visited)

print('supposed output:')
print(answer)
print(min(steps))
