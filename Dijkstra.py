def find_min(start,n_city,collected,mat,dist):
	min_dist = 501
	min_city = -1
	for i in range(n_city):
		if mat[pos(start,i)] != 501 and not collected[i]:
			if mat[pos(start,i)][0]<min_dist:
				min_city = i
				min_dist = mat[pos(start,i)][0]
	return min_city

def pos(a,b):
	if a>=b:
		return int(b+a*(a+1)/2)
	else:
		return int(a+b*(b+1)/2)

def main():
	a1 = [int(x) for x in input().split()]
	n_city = a1[0]
	n_ways = a1[1]
	start = a1[2]
	end = a1[3]
	mat = [501]*int(n_city*(n_city+1)/2)
	ways = []
	for i in range(n_ways):
		ways.append([int(x) for x in input().split()])
		mat[pos(ways[-1][0],ways[-1][1])] = ways[-1][2:]
	if n_city==2:
		print(ways[0][2],ways[0][3])
		return
	dist = n_city*[501]
	cost = n_city*[-1]
	collected = n_city*[False]
	collected[start] = True
	dist[start],cost[start] = 0,0
	for i in range(n_city):
		x = pos(start,i)
		if mat[x]!=501:
			dist[i],cost[i] = mat[x][0],mat[x][1]
	while True:
		city = find_min(start,n_city,collected,mat,dist)
		if city == -1:
			break
		collected[city] = True
		for i in range(n_city):
			if not collected[i] and mat[pos(city,i)] != 501:
				if dist[i]>mat[pos(city,i)][0]+dist[city]:
					dist[i] = mat[pos(city,i)][0]+dist[city]
					cost[i] = mat[pos(city,i)][1]+cost[city]
				elif dist[i]==mat[pos(city,i)][0]+dist[city]:
					cost[i] = min(cost[i],mat[pos(city,i)][1]+cost[city])
	print(dist[end],cost[end])	
main()