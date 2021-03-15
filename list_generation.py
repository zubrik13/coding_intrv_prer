input = '1238'
n = 3

z = [int(i) for i in input.split()]

a = [[0] * n for i in range(n)]
b = [[0 for j in range(n)] for i in range(n)]
c = list(map(lambda i: [0]*n, range(n)))

print z

print a
print b
print c