def insert_min(hea,x):
	if hea[-1] != None:
		return False
	for i in range(len(hea)):
		if hea[i] == None:
			k = i
			break
		else:
			continue
	hea[k] = x
	while True:
		if x > hea[k//2]:
			break
		elif x < hea[k//2]:
			hea[k] = hea[k//2]
			k = k//2
			hea[k] = x
	return hea

def insert_max(hea,x):
	if hea[-1] != None:
		return False
	for i in range(len(hea)):
		if hea[i] == None:
			k = i
			break
		else:
			continue
	hea[k] = x
	while True:
		if x < hea[k//2]:
			break
		elif x > hea[k//2]:
			hea[k] = hea[k//2]
			k = k//2
			hea[k] = x
	return hea

#返回最后一个元素的位置，也就是size。
def get_size(hea):
	k = 0
	while k < len(hea):
		if hea[k]!=None:
			k = k+1
		else:
			break
	return k-1

def build_max(keys,hea):
	j = insert_max(hea,keys[0])
	for x in keys[1:]:
		j = insert_max(j,x)
	return j

def build_min(keys,hea):
	j = insert_min(hea,keys[0])
	for x in keys[1:]:
		j = insert_min(j,x)
	return j

def delete_max(hea):
	tmp = hea[1]
	size = get_size(hea)
	hea[1] = hea[size]
	hea[size] = None
	size = size-1
	k = 1
	while (2*k+1)<=size:
		if (hea[k] > hea[2*k]) and (hea[k] > hea[2*k+1]):
			break
		elif (hea[k] < hea[2*k]) or (hea[k] < hea[2*k+1]):
			x = hea[k]
			hea[k] = max(hea[2*k],hea[2*k+1])
			if hea[k]==hea[2*k]:
				hea[2*k] = x
				k = k*2
			elif hea[k]==hea[2*k+1]:
				hea[2*k+1] = x
				k = k*2+1
	return hea	

def delete_min(hea):
	tmp = hea[1]
	size = get_size(hea)
	hea[1] = hea[size]
	hea[size] = None
	size = size-1
	k = 1
	while (2*k+1)<=size:
		if (hea[k] < hea[2*k]) and (hea[k] < hea[2*k+1]):
			break
		elif (hea[k] > hea[2*k]) or (hea[k] > hea[2*k+1]):
			x = hea[k]
			hea[k] = min(hea[2*k],hea[2*k+1])
			if hea[k]==hea[2*k]:
				hea[2*k] = x
				k = k*2
			elif hea[k]==hea[2*k+1]:
				hea[2*k+1] = x
				k = k*2+1
	return hea	


def path(pos,hea):
	res = []
	if len(hea)==1:
		return False
	while pos>=1:
		res = res+[hea[pos]]
		pos = pos//2
	return res

