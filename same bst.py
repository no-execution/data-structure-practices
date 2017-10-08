class tr(object):
    
    def __init__(self,data=None):
        self.right = None
        self.left = None
        self.data = data
        self.flag = 0

#查找元素(输入待查值和根节点，返回目标节点)
def find(tar,root):
    if not root:
        return None
    if tar > root.data:
        return find(tar,root.right)
    if tar < root.data:
        return find(tar,root.left)
    if tar == root.data:
        return root

#查找最小值(输入根节点，返回目标节点)
def find_min(root):
    k = root
    while k.left:
        k = k.left
    return k

#插入元素(输入根节点和待插入元素，返回完成插入后的树的根节点)
def insert(root,tar):
    if not root:
        return tr(tar)
    if tar > root.data:
        root.right = insert(root.right,tar)
    if tar < root.data:
        root.left = insert(root.left,tar)
    return root    

#删除元素(输入根节点和待删除元素，返回删除完成后的树的根节点)
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

#建立树(输入一个arraylist，返回建成后的树的根节点)
def build(lis):
    ro = tr(lis[0])
    for x in lis[1:]:
        insert(ro,x)
    return ro

#获得输入
def inp():
    k = [int(x) for x in input().split()]
    if k[0] == 0:
        return False
    if k[0]!=0:
        le = int(k[0])
        num = int(k[1])
    lis = []
    for i in range(num+1):
        lis.append([int(x) for x in input().split()])
    return lis

#把输入给格式化,获得一个三维数组[多个树[多组序列[序列]]]
def get_inp():
    trs = []
    a = inp()
    while a:
        trs.append(a)
        a = inp()
    return trs

#每次检查最内层数组的一个值
def check(root,tar):
        if not root:
            return False
        if tar == root.data:
            root.flag = 1
            return True
        if tar > root.data:
            if not root.flag:
                return False
            return check(root.right,tar)
        if tar < root.data:
            if not root.flag:
                return False
            root.flag = 1
            return check(root.left,tar)
                
def main():
    k = get_inp()
    for tree_list in k:
        for tree_child_list in tree_list[1:]:
            st = build(tree_list[0])
            si = 1
            for x in tree_child_list: 
                if not check(st,x):
                    si = 0
                    break
            if si:
                print('Yes')
            else:
                print('No')
main()
