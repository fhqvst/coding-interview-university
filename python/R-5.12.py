n = 100
matrix = [ [1] * n for k in range(n) ]

s = sum([ sum(row) for row in matrix ])
print(s)
