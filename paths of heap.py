def get_size():
	li = [int(x) for x in input().split()]
	return li

def get_keys():
	kk = [int(x) for x in input().split()]
	return kk

def get_start():
	st = [int(x) for x in input().split()]
	return st

def insert(hea,x):
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

def build(keys,hea):
	j = insert(hea,keys[0])
	for x in keys[1:]:
		j = insert(j,x)
	return j

def path(pos,hea):
	res = []
	if len(hea)==1:
		return False
	while pos>=1:
		res = res+[hea[pos]]
		pos = pos//2
	return res

def main():
	pre = get_size()
	size = pre[0]
	ways = pre[1] 
	heap = [-10001]+[None]*(size)
	keys = get_keys()
	begins = get_start()
	new_heap = build(keys,heap)
	mid = []
	for x in begins:
		mid.append(path(x,new_heap))
	for s in mid:
		print(" ".join([str(x) for x in s]))

main()
