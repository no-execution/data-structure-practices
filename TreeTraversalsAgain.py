n = int(input())
inp = []
for i in range(2*n):
    inp.append([x for x in input().split()])

def get_in(array):
    in_order = []
    stack = []
    for i in range(len(array)):
        if array[i][0]=='Push':
            stack.append(array[i][1])
        if array[i][0]=='Pop':
            in_order.append(stack.pop())
    return in_order
            
def get_pre(array):
    pre_order = []
    for i in range(len(array)):
        if array[i][0]=='Push':
            pre_order.append(array[i][1])
        else:
            continue
    return pre_order

def get_post(pre,mid,a):
    if len(pre)==1:
        return a.append(pre[0])
    if len(pre)==0:
        return
    root = pre[0]
    root_index = mid.index(root)
    get_post(pre[1:root_index+1],mid[:root_index],a)
    get_post(pre[root_index+1:],mid[root_index+1:],a)
    a.append(root)
    return a

p = get_pre(inp)
m = get_in(inp)
print(get_post(p,m,[]))
