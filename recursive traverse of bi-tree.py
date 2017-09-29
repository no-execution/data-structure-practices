class Tree(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

node1 = Tree(1)
node2 = Tree(2)
node3 = Tree(3)
node4 = Tree(4)
node5 = Tree(5)
root = node1

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

def pre_order(tree):
	if not tree:
		return 
	print(tree.data)
	pre_order(tree.left)
	pre_order(tree.right)

def in_order(tree):
	if not tree:
		return
	in_order(tree.left)
	print(tree.data)
	in_order(tree.right)

def post_order(tree):
	if not tree:
		return
	post_order(tree.left)
	post_order(tree.right)
	print(tree.data)

