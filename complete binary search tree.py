k = 0

def inp_n():
	return int(input())

def inp_node():
	return [int(x) for x in input().split()]

def build(root,tree,node,n):
	global k
	if root>n:
		return None
	build(2*root,tree,node,n)
	tree[root] = node[k]
	k = k+1
	build(2*root+1,tree,node,n)
	return tree

def main():
	n1 = inp_n()
	nod = inp_node()
	nod.sort()
	tree = [1 for i in range(n1+1)]
	kk = build(1,tree,nod,n1)
	return kk

a = main()
print(" ".join(str(x) for x in a[1:]))
