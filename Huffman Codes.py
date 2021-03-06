class tr(object):
 	def __init__(self,data=0):
 		self.left = None
 		self.right = None
 		self.data = data
 		self.flag = 0

#获得编码的字符数。
def get_nums_codes():
	return int(input())

#获得待验证编码的组数。
def get_nums_lists():
	return int(input())

#返回包括四个字典的列表{字符：二进制编码}。
def get_codes(n_codes,n_lists):
	res = []
	for i in range(n_lists):
		keys = []
		vals = []
		for j in range(n_codes):
			mid = [x for x in input().split()]
			keys.append(mid[0])
			vals.append(mid[1])
		dic = {}.fromkeys(keys)	
		for x in range(n_codes):
			dic[keys[x]] = vals[x] 
		res.append(dic)
	return res	

#获得各字符，及其出现的频率,返回一个字典。
def get_fre(n):
	i = 0
	key = []
	val = []
	mid = [x for x in input().split()]
	for j in range(n):
		key.append(mid[j*2])
		val.append(int(mid[j*2+1]))
	fre = {}.fromkeys(key)
	for i in range(n):
		fre[key[i]] = val[i]
	return fre

#通过二进制的编码建立二叉树
#每次检查编码都应该从已有的树根开始
def build_by_code(code):
	root = tr()
	res = root
	for y in code:
		root = res
		for x in y:
			if x=="0" and not root.left:
				root.left = tr()
				root = root.left
				continue
			if x == "0" and root.left:
				root = root.left
				continue
			if x == "1" and not root.right:
				root.right = tr()
				root = root.right
				continue
			if x == "1" and root.right:
				root = root.right
				continue
	return res

#计算权值，通过数组,每次计算一组
def cal_by_list(dic,fre):
	res = 0
	for key in dic:
		zhi = len(dic[key])
		rate = fre[key]
		res = res+(zhi*rate)
	return res

#计算huffman树的wpl。
def cal_by_tree(ht):
	q = []
	res = []
	lay = 0
	q.append(ht)
	while q!=[]:
		k = q.pop()
		if k.left or k.right:
			res.append(k.data)
		if k.left:
			q.insert(0,k.left)
		if k.right:
			q.insert(0,k.right)
		else:
			continue                             
	return sum(res)

#前缀检查。每次检查一组编码,需要一个编码(字符串)的二进制以及相应的哈夫曼树
def pre_check(codes,root):
	res = True
	mid = root
	for x in codes:
		root = mid
		for k in x:
			if k == '0':
				root = root.left
			else:
				root = root.right
		if root.flag == 1:
			res = False
		if root.left or root.right:
			res = False
			break
		else:
			root.flag = 1
			continue
	return res

#建立huffman树。
def build_huf(hea):
    while hea[2]:
    	left = hea[1]
    	hea = delete_min(hea)
    	right = hea[1]
    	hea = delete_min(hea)
    	par = tr(left.data+right.data)
    	par.left = left
    	par.right = right
    	hea = insert_min(par,hea)
    return hea[1]

#获得最小堆的size
def get_size(hea):
	k = 0
	while k < len(hea):
		if hea[k]!=None:
			k = k+1
		else:
			break
	return k-1

#删除最小堆的根。
def delete_min(hea):
	tmp = hea[1]
	size = get_size(hea)
	hea[1] = hea[size]
	hea[size] = None
	size = size-1
	x = hea[1]
	k = 1
	while (2*k)<=size:
		c = k*2
		if (c != size) and (hea[c].data>hea[c+1].data):
			c = c+1
		if x.data<hea[c].data:
			break
		else:
			hea[k] = hea[c]
		k = c
	hea[k] = x
	return hea	

#输入一个数字组成的数组，返回一个节点组成的数组。
def create_node(lis):
 	res = []
 	for x in lis:
 		res.append(tr(x))
 	return res

#hea是由节点组成的堆,要求初始化堆时第一个值非常小,返回插入后的堆。
def insert_min(nod,hea):
	if hea[-1] != None:
		return False
	for i in range(len(hea)):
		if hea[i] == None:
			k = i
			break
		else:
			continue
	hea[k] = nod
	while True:
		if hea[k].data >= hea[k//2].data:
			break
		elif hea[k].data < hea[k//2].data:
			x = hea[k]
			hea[k] = hea[k//2]
			hea[k//2] = x
			k = k//2
	return hea

#建立最小堆。
def build_min(nodes,hea):
	j = insert_min(nodes[0],hea)
	for x in nodes[1:]:
		j = insert_min(x,j)
	return j

def main():
	#1.通过fre建堆
	n1 = get_nums_codes()   #每组的编码数
	heap = [tr(-1)]+n1*[None]
	fre = get_fre(n1)
	lis = []      			#出现的频数
	for key in fre:
		lis.append(fre[key])
	nodes = create_node(lis)
	r = build_min(nodes,heap)
	huf_tree = build_huf(r)
	n2 = get_nums_lists()   #待查组的个数
	#2.由建好的堆建huffman树,算出最小权值。
	standard = cal_by_tree(huf_tree)
	#3.通过最小权值检查各组树
	code_and_key = get_codes(n1,n2)
	min_nums = []
	val_check = n2*[True] 
	for dicts in code_and_key:   
		min_nums.append(cal_by_list(dicts,fre))

	for i in range(len(min_nums)):
		if min_nums[i] != standard:
			val_check[i] = False
	#4.通过二进制编码建树，之前未通过的编码组就不用建了。
	bianma = n2*[None]
	code_root = n2*[None]
	for i in range(len(code_and_key)):
		if val_check[i] == False:
			continue
		song = []
		for key in code_and_key[i]:
			if len(code_and_key[i][key])>63:
				song = False
				break
			song.append(code_and_key[i][key])
		bianma[i] = song
		code_root[i] = build_by_code(song)
	#5.对通过的编码进行前缀检查。
	for i in range(len(code_root)):
		#函数每次检查一个根节点。
		if not code_root[i]:
			continue
		if not bianma[i]:
			continue
		else:
			val_check[i] = pre_check(bianma[i],code_root[i])
	#6.若同时通过前缀检查和权值检查则打印yes,否则
	for z in val_check:
		if z:
			print('Yes')
		else:
			print('No')
main()
