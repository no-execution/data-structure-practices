pre = [int(x) for x in input().split()]
size = pre[0]  #size of stack
nums = pre[1]  #length of the list of numbers 
n = pre[2]     #quantities of lists    
lists = []
for i in range(n):
    lists.append([int(x) for x in input().split()])

def add(li,a,b):
    for i in range(a,b):
        li.append(i)
    return li

def check(lis,n):
    i = 1
    stack = []
    for x in lis:
        if i > x:
            if stack[-1] != x or len(stack)==0:
                return 'NO'
            else:
                stack.pop()
                continue
        if i <= x:
            if len(stack)+(x+1-i)>n:
                return 'NO'
            else:
                add(stack,i,x+1)
                i = x+1
                if i > x:
                    stack.pop()
                else:
                    continue
    return 'YES'


for i in range(n):
    print(check(lists[i],size))
