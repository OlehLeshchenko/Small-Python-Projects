graph = [[1, 3],[0, 2, 3, 4],[1, 4, 5],[0, 1, 4, 6],[1, 2, 3, 7],[2, 8],[3],[4],[5]]
pozhat = [-1]*len(graph)
print("Початковий стан", pozhat)
print("Динаміка зміни стану перегляду вершин")
def func(s):
    global pozhat
    pozhat[s] = 0
    zherg = [s]
    while zherg:
        print(pozhat)
        v = zherg.pop(0)
        for i in graph[v]:
            if pozhat[i] ==  -1:
                zherg.append(i)
                pozhat[i] = pozhat[v]+1
for i in range(len(graph)):
    if pozhat[i] == -1:
        func(i)
    print("Вершина", i, ", номер обходу", pozhat[i])
        
