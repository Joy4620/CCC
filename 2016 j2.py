grid = [list(map(int, input().split())) for _ in range(4)]
total = sum(grid[0])
output = 'magic'
for j in range(4):
    if sum([grid[i][j] for i in range(4)]) != total:
        output = 'not magic'
    if sum(grid[j]) != total:
        output = 'not magic'
print(output)
