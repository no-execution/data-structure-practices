class tr(object):
    
    def __init__(self,data=None):
        self.right = None
        self.left = None
        self.data = data


def find(tar,root):
    if not root:
        return None
    if tar > root.data:
        return find(tar,root.right)
    if tar < root.data:
        return find(tar,root.left)
    if tar == root.data:
        return root

def find_min(root):
    k = root
    while k.left:
        k = k.left
    return k

def insert(root,tar):
    if not root:
        return tr(tar)
    if tar > root.data:
        root.right = insert(root.right,tar)
    if tar < root.data:
        root.left = insert(root.left,tar)
    return root    

def delete(root,tar):
    tmp = tr()
    if not root:
        return None
    if tar > root.data:
        root.right = delete(root.right,tar)
    if tar < root.data:
        root.left = delete(root.left,tar)
    else:
        if root.right and root.left:
            tmp = find_min(root.right)
            root.data = tmp.data
            root.right = delete(root.right,root.data)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
    return root

def build(lis):
    ro = tr(lis[0])
    for x in lis[1:]:
        insert(ro,x)
    return ro


