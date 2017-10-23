def get_position(n):
	res = []
	for i in range(n):
		res.append([int(x) for x in input().split()])
	return res


def connect(pos,d):
	res = []
	for i in range(len(pos)):
		for j in range(len(pos)):
			if i == j:
				continue
			elif ((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2) <= d**2:
				res.append([i,j])
	return res

def build_mat(edges,n):
	res = int(n*(n+1)/2)*[0]
	for x in edges:
		if x[0]>x[1]:
			pos = x[1]+(x[0]*(1+x[0]))/2
		else:
			pos = x[0]+(x[1]*(1+x[1]))/2
		res[int(pos)] = 1
	return res

#给出节点坐标和蹦多远，返回节点编号。		
def get_start(pos,d):
	res = []
	for i in range(len(pos)):
		if pos[i][0]**2+pos[i][1]**2<=(7.5+d)**2:
			res.append(i)
		else:
			continue
	return res

def broad_first(mat,start,n,visited,position,d):
	que = []
	visited[start] = 1
	que.insert(0,start)
	res = []
	while que!=[]:
		k = que.pop()
		if position[k][0]>=(50-d) or position[k][1]>=(50-d) or position[k][0]<=(d-50) or position[k][1]<=(d-50):
			return True
		res.append(k)
		for i in range(n):
			if k > i:
				pos = i+(k*(k+1))/2
			else:
				pos = k+(i*(i+1))/2
			if mat[int(pos)] == 1 and visited[i] != 1:
				que.insert(0,i)
				visited[i] = 1
			else:
				continue
	return [False,visited]

def deep_first(mat,n,visited,start,res,position,d):
	visited[start] = 1
	if position[start][0]>=(50-d) or position[start][1]>=(50-d) or position[start][0]<=(d-50) or position[start][1]<=(d-50):
		res = True
	for i in range(n):
		if start>i:
			pos = i+(start*(start+1))/2
		else:
			pos = start+(i*(i+1))/2
		if mat[int(pos)] == 1 and visited[i] != 1:
			deep_first(mat,n,visited,i,res,position,d)
		else:
			continue
	return [res,visited]

def main():
	k = [int(x) for x in input().split()]
	n_node = k[0]
	distance = k[1]
	nodes = get_position(n_node)
	#建立邻接矩阵？
	#space = n_node*(n_node+1)/2
	edges = connect(nodes,distance)
	mat = build_mat(edges,n_node)
	visited = n_node*[0]
	start_nodes = get_start(nodes,distance)
	while visited != n_node*[1]:
		if len(start_nodes) == 0:
			res = False
			break
		for x in start_nodes:
			if visited[x]==0:
				start = x
				break
		q = deep_first(mat,n_node,visited,start,None,nodes,distance)
		if q[0]==True :
			res = True
			print(res)
			break
		else:     
			visited = q[1]       
			res = q[0]
			continue              
	if res:                     
		print('Yes')
	else:
		print('No')
main()
