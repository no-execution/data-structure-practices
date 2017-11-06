def bfs_change(n_node,start,zuobiao,distance,path,dist):
	que = []
	if dist[start] == -1:
		dist[start] = 1
	else:
		return path,dist
	que.append(start)
	while que!=[]:
		k = que.pop()
		for i in range(n_node):
			if ((zuobiao[k][0]-zuobiao[i][0])**2+(zuobiao[k][1]-zuobiao[i][1])**2)<=distance**2:
				if dist[i] == -1:
					dist[i] = dist[k]+1   
					path[i] = k           
					que.insert(0,i)
	return path,dist

def main():
	a1 = [x for x in input().split()]	
	n_node = int(a1[0])
	distance = float(a1[1])
	if distance>=42.5:
		print('1')
		return
	zuobiao = []
	start_nodes = [] #存第一落脚点的下标
	path = n_node*[-1]
	dist = n_node*[-1]
	for i in range(n_node):
		zuobiao.append([int(x) for x in input().split()])
	for i in range(len(zuobiao)):
		if (distance+7.5)**2 >= (zuobiao[i][0]**2+zuobiao[i][1]**2) and (zuobiao[i][0]**2+zuobiao[i][1]**2)>=7.5**2:
			start_nodes.append([i,zuobiao[i][0]**2+zuobiao[i][1]**2])
	for x in start_nodes:
		path,dist = bfs_change(n_node,x[0],zuobiao,distance,path,dist)
	shangan = -2
	for i in range(n_node):
		if dist[i]==-1:
			continue
		if zuobiao[i][0]>=(50-distance) or zuobiao[i][0]<=(distance-50) or zuobiao[i][1]>=(50-distance) or zuobiao[i][1]<=(distance-50):
			if shangan == -2:
				shangan = i
			elif dist[shangan]>dist[i]:
				shangan = i
			elif dist[shangan]==dist[i]:
				k = i
				q = shangan
				while dist[k]!=1:
					k = path[k]
				while dist[q]!=1:
					q = path[q]
				if zuobiao[k][0]**2+zuobiao[k][1]**2<zuobiao[q][0]**2+zuobiao[q][1]**2:
					shangan = i 
	if shangan == -2:
		print('0')
		return 
	else:
		stack = []
		stack.append(shangan)
		stack.append(path[shangan])
		flag = path[shangan]
		while dist[flag]!=1:
			stack.append(path[flag])
			flag = path[flag]
		print(len(stack)+1)
		while stack!=[]:
			print(" ".join([str(x) for x in zuobiao[stack.pop()]]))	
main()

