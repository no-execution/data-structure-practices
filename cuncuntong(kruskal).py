def pos(a,b):
	if a>=b:
		return int(b+a*(a+1)/2)
	else:
		return int(a+b*(b+1)/2)

#小的往大的并
def union(v1,v2,set_city):
	if set_city[v1] >= set_city[v2]:
		set_city[v2] += set_city[v1]
		set_city[v1] = v2
	else:
		set_city[v1] += set_city[v2]
		set_city[v2] = v1
	return set_city


def find_set(v,set_city):
	k = v
	while set_city[v]>=0:
		v = set_city[v]
	if k!=v:
		set_city[k] = v
	return v,set_city

def get_size(hea):
	k = 0
	while k < len(hea):
		if hea[k]!=None:
			k = k+1
		else:
			break
	return k-1

def build_heap(hea,ways):
	j = insert_min(hea,ways[0])
	for x in ways[1:]:
		j = insert_min(j,x)
	return j


def insert_min(hea,x):
	if hea[-1] != None:
		return False,False
	for i in range(len(hea)):
		if hea[i] == None:
			k = i
			break
	hea[k] = x
	while True:
		if x[2] >= hea[k//2][2]:
			break
		elif x[2]<hea[k//2][2]:
			hea[k] = hea[k//2]
			k = k//2   
			hea[k] = x
	return hea

#有问题
def delete_min(hea,n_ways):
	if hea == [[-1,-1,-1]]+n_ways*[None]:
		return False,False
	tmp = hea[1]
	size = get_size(hea)
	hea[1] = hea[size]
	hea[size] = None
	size = size-1
	#向下调整
	k = 1
	while k*2<=size:
		child = k*2
		if k*2 != size and hea[k*2+1][2]<hea[k*2][2]:
			child = k*2+1
		if hea[k][2]<=hea[child][2]:
			k = child
			break
		else:
			x = hea[k]
			hea[k] = hea[child]
			hea[child] = x
			k = child
	return hea,tmp            #tmp是根节点的数组。 


def main():
	start = 0
	info = [int(x) for x in input().split()]
	n_city,n_ways = info[0],info[1]
	if n_ways< n_city-1:
		print(-1)
		return
	ways = []
	set_city = n_city*[-1]   #并查集用边？还是点？
	for i in range(n_ways):
		ways.append([int(x) for x in input().split()]+[i])
	#最小堆的初始化,从1开始
	hea = [[-1,-1,-1]]+n_ways*[None]
	hea = build_heap(hea,ways)
	flag = 0
	power = 0
	while flag<n_city-1:
		hea,way = delete_min(hea,n_ways)
		if not hea:
			break
		v1,v2 = way[0]-1,way[1]-1
		tmp = way[2]
		k1,set_city = find_set(v1,set_city)
		k2,set_city = find_set(v2,set_city)
		if k1 == k2:
			continue
		else:
			set_city = union(k1,k2,set_city)
			power += tmp
			flag += 1
	if flag!=n_city-1:
		print(-1)
	else:
		print(power)
main()