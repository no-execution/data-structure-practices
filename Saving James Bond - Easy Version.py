def get_position(n):
	res = []
	for i in range(n):
		res.append([int(x) for x in input().split()])
	return res

def get_start(pos,d):
	res = []
	for i in range(len(pos)):
		if pos[i][0]**2+pos[i][1]**2<=(7.5+d)**2:
			res.append(i)
		else:
			continue
	return res

def deep_first(n,visited,start,res,position,d):
	visited[start] = 1
	if position[start][0]>=(50-d) or position[start][1]>=(50-d) or position[start][0]<=(d-50) or position[start][1]<=(d-50):
		res.append(True)
		return [res,visited]
	for i in range(n):
		if ((position[i][0]-position[start][0])**2+(position[i][1]-position[start][1])**2)<=d**2 and visited[i] != 1:
			deep_first(n,visited,i,res,position,d)
		else:
			continue
	return [res,visited]

def main():
	k = [int(x) for x in input().split()]
	n_node = k[0]
	distance = k[1]
	nodes = get_position(n_node)
	visited = n_node*[0]
	start_nodes = get_start(nodes,distance)
	res = False
	while visited!=n_node*[1]:
		if len(start_nodes) == 0:
			break
		for x in start_nodes:
			if visited[x]==0:
				start = x
				break
			else:
				start = None
		if not start:
			if start !=0:
				break
		q = deep_first(n_node,visited,start,[],nodes,distance)
		visited = q[1]       
		re = q[0]   
		for x in re:
			if x:
				res = True
				break
	if distance>=42.5:
		res = True
	if res:                     
		print('Yes')
	else:
		print('No')
main()
