def pos(a,b):
	if a>=b:
		return int(b+a*(a+1)/2)
	else:
		return int(a+b*(b+1)/2)

def find_min(n,dist):
	min_dist = 'max'
	k = -1
	for i in range(n):
		if dist[i] == 'max':
			continue
		if dist[i]!=0 and min_dist=='max':
			min_dist = dist[i]
			k = i
		if dist[i]>0 and dist[i]<min_dist:
			min_dist = dist[i]
			k = i
	return k

def prim(start,n_city,dist,mat):
	mst,power = 0,0
	while True:
		v = find_min(n_city,dist)
		if v == -1:
			break
		power += dist[v]
		dist[v] = 0
		mst += 1
		for i in range(n_city):
			po = pos(v,i)
			if dist[i]!=0 and mat[po]!=-1:
				dist[i] = mat[po]
	return power,mst

def main():
	start = 0
	info = [int(x) for x in input().split()]
	n_city,n_ways = info[0],info[1]
	ways = []
	for i in range(n_ways):
		ways.append([int(x) for x in input().split()])
	dist = ['max']*n_city
	dist[0] = 0
	mat = [-1]*int(n_city*(n_city+1)/2)	
	for x in ways:
		mat[pos(x[0]-1,x[1]-1)] = x[2]
	for i in range(1,n_city):
		po = int(i*(i+1)/2)
		if mat[po] != -1:
			dist[i] = mat[po]
	k = prim(start,n_city,dist,mat)
	if k[1] == n_city-1:
		print(k[0])
	else:
		print(-1)

main()