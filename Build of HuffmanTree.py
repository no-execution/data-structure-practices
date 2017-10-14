class tr(object):

 	def __init__(self,data=0):
 		self.left = None
 		self.right = None
 		self.data = data

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

def get_size(hea):
	k = 0
	while k < len(hea):
		if hea[k]!=None:
			k = k+1
		else:
			break
	return k-1

def delete_min(hea):
	tmp = hea[1]
	size = get_size(hea)
	hea[1] = hea[size]
	hea[size] = None
	size = size-1
	k = 1
	while (2*k+1)<=size:
		if (hea[k].data < hea[2*k].data) and (hea[k].data < hea[2*k+1].data):
			break
		elif (hea[k].data > hea[2*k].data) or (hea[k].data > hea[2*k+1].data):
			x = hea[k]
			hea[k] = tr(min(hea[2*k].data,hea[2*k+1].data))
			if hea[k].data==hea[2*k].data:
				hea[2*k] = x
				k = k*2
			elif hea[k].data==hea[2*k+1].data:
				hea[2*k+1] = x
				k = k*2+1
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
		if hea[k].data > hea[k//2].data:
			break
		elif hea[k].data < hea[k//2].data:
			x = hea[k]
			hea[k] = hea[k//2]
			hea[k//2] = x
			k = k//2
	return hea

def build_min(nodes,hea):
	j = insert_min(nodes[0],hea)
	for x in nodes[1:]:
		j = insert_min(x,j)
	return j

heap = [tr(-1)]+[None]*5
q = create_node([46,26,24,23,10])
r = build_min(q,heap)
k = build_huf(r)

