from collections import deque

N=int(input())
g=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def bfs(s):
    d=deque([s])
    v=[10**10]*N
    v[s]=0
    while len(d):
        now=d.pop()
        for i in g[now]:
            if v[i]!=10**10:continue
            v[i]=v[now]+1
            d.append(i)
    m=max(v)
    for i in range(N):
        if v[i]==m: return (m,i)
print(bfs(bfs(0)[1])[0]+1)
