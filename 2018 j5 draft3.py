class Point():
    def __init__(self, x, parent=None):
        self.x = x
        self.step = 1
        self.record=[x]
        if parent:
            self.step = parent.step + 1
            self.record=parent.record+self.record

N = int(input())
book = {i: set(map(int, input().split()[1:])) for i in range(1, N + 1)}
Stack = [Point(1)]
visited = set()
steps = set()

while Stack:
    P = Stack.pop(0)
    if P in visited:
        continue
    visited.add(P.x)
    if not book[(P.x)]:
        steps.add(P.step)
        continue
    for i in book[P.x]:
        Stack.append(Point(i, P))

print('Y') if len(visited) == N else print('N')
print(min(steps))
