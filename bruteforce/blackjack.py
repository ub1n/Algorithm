import sys
from itertools import combinations
import heapq

n = sys.stdin.readline().split()
card=sys.stdin.readline().split()
n=list(map(lambda x:int(x),n))
card=list(map(lambda x:int(x),card))
m=list(combinations(card,3))
heap=[]
for i in m:
    s=sum(i)
    if s<=n[1]:
        heapq.heappush(heap,-s)
print(-heapq.heappop(heap))