import sys
input = sys.stdin.readline
print = sys.stdout.write

R, C, Q = map(int, input().split())
graph = [[float('inf')] * C for _ in range(R)]

cur = {}
out = set()

def process(cmd, id):
    if cmd == "In":
        if id in cur:
            print(f'{id} already seated.')
        elif id in out:
            print(f'{id} already ate lunch.')
        else:
            r, c = 0, 0
            mindist = 0
            for i in range(R):
                for j in range(C):
                    if graph[i][j] > mindist:
                        r, c = i, j
                        mindist = graph[i][j]
            if mindist == 1:
                print("There are no more seats.")

    else:
        if id not in cur:
            print(f'{id} didn\'t eat lunch.')
        elif id in out:
            print(f'{id} already left seat.')
        else:
            r, c = cur[id]
            