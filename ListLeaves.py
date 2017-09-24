data = 0
left = 1
right = 2
n = int(input())
tr = []
leaves = []
def gen(tree,n):
    biao = [0]*n
    for i in range(n):
        if tree[i][left]!=-1:
            biao[tree[i][left]] = 1
        if tree[i][right]!=-1:
            biao[tree[i][right]] = 1
        else:
            continue
    for i in range(n):
        if biao[i]==0:
            return i
        else:
            continue

def sortt(tree,root,n):
    res = []
    que = []
    while len(res)!=n:
        if que == []:
            que.insert(0,tree[root])  #用insert入队,这样list的头为队尾,list的尾
        while que!=[]:                #为队头,进队用insert，出队用pop                  
            k = que.pop()
            res.append(k)
            if k[left] != -1:
                que.insert(0,tree[k[left]])
            if k[right] != -1:
                que.insert(0,tree[k[right]])
            else:
                continue        
    return res



for i in range(n):
    k=[]
    q = input().split()
    k.append(i)
    if q[0] != '-':
        k.append(int(q[0]))
    else:
        k.append(-1)
    if q[1] != '-':
        k.append(int(q[1]))
    else:
        k.append(-1)
    tr.append(k)
root = gen(tr,n)
mid = sortt(tr,root,n)

for i in range(len(mid)):
    if mid[i][left]==-1 and mid[i][right]==-1:
        leaves.append(mid[i][0])
        
print(" ".join([str(x) for x in leaves]))
