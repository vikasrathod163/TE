# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1':set(['2','3','4']),
         '2':set(['1','5']),
         '3':set(['1','6']),
         '4':set(['1','7']),
         '5':set(['2','8']),
         '6':set(['3','9']),
         '7':set(['4','10']),
         '8':set(['5']),
         '9':set(['6']),
        '10':set(['7'])
         }




dfs(graph, '1')


'''gescoe@gescoe-OptiPlex-3020:~$ cd TE-B37
gescoe@gescoe-OptiPlex-3020:~/TE-B37$ python3 ass1dfs.py
1
4
7
10
3
6
9
2
5
8
gescoe@gescoe-OptiPlex-3020:~/TE-B37$ '''

