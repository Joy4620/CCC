N = int(input())
k = int(input())
count = N
var = str(N)
for i in range(k):
    count += int(var + '0')
    var += '0'
print(count)
