data = 0
left = 1
right = 2
tr1 = []
tr2 = []
def inp(info):
    mid = []
    mid.append(info[0])
    if info[1]!='-':
        mid.append(int(info[1]))
    else:
        mid.append(-1)
    if info[2]!='-':
        mid.append(int(info[2]))
    else:
        mid.append(-1)
    return mid


def gen(tree,n):
    biao = [0]*n+[None]
    for i in range(n):
        if tree[i][1]!=-1:
            biao[tree[i][1]]=1
        if tree[i][2]!=-1:
            biao[tree[i][2]]=1
        else:
            continue
    for i in range(n):
        if biao[i]==0:
            return i

def check(t1,t2,tree1,tree2):
    if ((t1 == None) and (t2 == None)):
        return 1
    if (((t1 == None) and (t2 != None)) or ((t1 != None) and (t2 == None))):
        return 0
    if t1[data]!=t2[data]:
        return 0
    if((t1[left] == -1) and (t2[left] == -1)):
        return (check(tree1[t1[right]],tree2[t2[right]],tree1,tree2))
    if((t1[left]!=-1 and t2[left]!=-1) and (tree1[t1[left]][data] == tree2[t2[left]][data])):
        return (check(tree1[t1[left]],tree2[t2[left]],tree1,tree2) and check(tree1[t1[right]],tree2[t2[right]],tree1,tree2))
    else:
        return (check(tree1[t1[left]],tree2[t2[right]],tree1,tree2) and check(tree1[t1[right]],tree2[t2[left]],tree1,tree2))
        
n1 = int(input())    
for i in range(n1):                  
    tr1.append(inp(input().split()))
tr1 = tr1+[None]
n2 = int(input())
for i in range(n2):
    tr2.append(inp(input().split()))
tr2 = tr2+[None]
if n1==0 and n2==0:
    print('Yes')
    exit(0)
if n1 != n2:
    print('No')
    exit(0)

root1 = gen(tr1,n1)
root2 = gen(tr2,n2)

res = check(tr1[root1],tr2[root2],tr1,tr2)

if res:
    print('Yes')
    exit(0)
else:
    print('No')

