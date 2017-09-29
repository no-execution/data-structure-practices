class Tree(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.lag = False

node1 = Tree(1)
node2 = Tree(2)
node3 = Tree(3)
node4 = Tree(4)
node5 = Tree(5)
node6 = Tree(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
root = node1

def pre_order(tree):
	stack = []
	res = []
	while tree or stack!=[]:
		while tree:
			stack.append(tree)
			res.append(tree.data)
			tree = tree.left
		k = stack.pop()		
		tree = k.right
	return res

def in_order(tree):
	stack = []
	res = []
	while tree or stack!=[]:
		while tree:
			stack.append(tree)
			tree = tree.left
		k = stack.pop()	
		res.append(k.data)	
		tree = k.right
	return res

def post_order(tree):
	stack = []
	res = []
	while tree or stack!=[]:
		while tree:
			stack.append(tree)
			tree = tree.left
		k = stack[-1]
		print(k)
		if k.lag:
			res.append(stack.pop().data)
			tree = None
			continue
		if not k.lag:
			k.lag = True
			tree = k.right
			continue
	return res		

def layer_order(tree):
	q = []
	res = []
	q.append(tree)
	while q!=[]:
		k = q.pop()
		res.append(k.data)
		if k.left:
			q.insert(0,k.left)
		if k.right:
			q.insert(0,k.right)
		else:
			continue                             
	return res

