d = [[0, 3, 5, 9, 10, 4], [3, 0, 0, 0, 8, 6], [5, 0, 0, 2, 11, 0], [9, 0, 2, 0, 0, 7], [10, 8, 11, 0, 0, 0], [4, 6, 0, 7, 0, 0]]
n = len(d)
for x in d:
  print(*x)
col=[i for i in range(n)] 
print(col)
s = 0
for k in range(n-1): 
  m=1000
  for i in range(n):
    for j in range(i+1,n):
      if col[i]!=col[j] and d[i][j]!=0 and d[i][j]<m: 
        m=d[i][j]
        t=i
        r=j
        g=col[i]
        h=col[j]
  s += m
  print(t+1,r+1)
  for i in range(n): 
    if col[i]==g: col[i]=h
print(s)
