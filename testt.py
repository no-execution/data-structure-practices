def bfs_change(n_node,start_nodes,zuobiao,distance):
	que = []
	path = n_node*[-1]
	dist = n_node*[-1]
	for x in start_nodes:
		dist[x] = 1
	while start_nodes!=[]:
		que.append(start_nodes.pop())
	while que!=[]:
		k = que.pop()
		for i in range(n_node):
			if i == k:
				continue
			if ((zuobiao[k][0]-zuobiao[i][0])**2+(zuobiao[k][1]-zuobiao[i][1])**2)<=distance**2:
				if dist[i] == -1:
					dist[i] = dist[k]+1
					path[i] = k
					que.insert(0,i)
	return path,dist



def main():	
	n_node = 17
	distance = 15
	zuobiao = [[10,-21],[10,21],[-40,10],[30,-50],[20,40],[35,10],[0,-10],[-25,22],[40,-40],[-30,30],[-10,22],[0,11],[25,21],[25,10],[10,10],[10,35],[-30,10]]
	start_nodes = [] #存第一落脚点的下标
	for i in range(len(zuobiao)):
		if (distance+7.5)**2 >= (zuobiao[i][0]**2+zuobiao[i][1]**2):
			start_nodes.append(i)
	path,dist = bfs_change(n_node,start_nodes,zuobiao,distance)

	#############################################
	shangan = -2
	for i in range(n_node):
		print(shangan)
		if dist[i]==-1:
			continue
		if zuobiao[i][0]>=(50-distance) or zuobiao[i][0]<=(distance-50) or zuobiao[i][1]>=(50-distance) or zuobiao[i][1]<=(distance-50):
			if shangan == -2:
				shangan = i
			elif dist[shangan]>=dist[i]:
				shangan = i
	if shangan == -2:
		print('0')
  #对于这个例子来说，shangan应该是12
	stack = []
	stack.append(path[shangan])
	flag = path[shangan]
	while dist[flag]!=1:
		stack.append(path[flag])
		flag = path[flag]
	while stack!=[]:
		print(zuobiao[stack.pop()])	
main()

