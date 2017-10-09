class tr(object):
    
    def __init__(self,data=None,height = 0):
        self.right = None
        self.left = None
        self.data = data
        self.height = height

#给出树的根节点，返回树的高度。
def get_height(root):
    if not root:
        return 0
    a = get_height(root.left)
    b = get_height(root.right)
    k = max(a,b)
    return k+1

def Left_Rotation(root):
	a = root
	b = a.left
	a.left = b.right
	b.right = a
	a.height = get_height(a)
	b.height = get_height(b)
	return b

def Right_Rotation(root):
	a = root
	b = a.right
	a.right = b.left
	b.left = a
	a.height = get_height(a)
	b.height = get_height(b)
	return b

#先把左右倾斜变成左倾斜，再把左倾斜通过LL变成平衡树。
def Left_Right(root):
	a = root
	a.left = Right_Rotation(a.left)
	return Left_Rotation(a)

def Right_Left(root):
	a = root
	a.right = Left_Rotation(a.right)
	return Right_Rotation(a)

def insert(x,root):
	if not root:
		return tr(x)
	elif x < root.data:
		root.left = insert(x,root.left)
		if (get_height(root.left)-get_height(root.right) == 2):
			if x < root.left.data:
				root = Left_Rotation(root)
			else:
				root = Left_Right(root)
	elif x > root.data:
		root.right = insert(x,root.right)
		if (get_height(root.right)-get_height(root.left) == 2):
			if x > root.right.data:
				root = Right_Rotation(root)
			else:
				root = Right_Left(root)
	root.height = get_height(root)
	return root

def inp():
    n = int(input())
    keys = [int(x) for x in input().split()]
    return keys

def main():
    nodes = inp()
    ro = None
    for x in nodes:
        ro = insert(x,ro)
    print(ro.data)
main()
