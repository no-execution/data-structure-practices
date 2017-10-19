def get_bian(n):
	res = []	
	for i in range(n):
		res.append([int(x) for x in input().split()])
	return res

def build_mat(edges,n):
	res = n*n*[0]
	for x in edges:
		if x[0]>x[1]:
			pos = x[1]+(x[0]*(1+x[0]))/2
		else:
			pos = x[0]+(x[1]*(1+x[1]))/2
		res[int(pos)] = 1
	return res

def deep_first(mat,n,visited,start,res):
	visited[start] = 1
	res.append(start)
	for i in range(n):
		if start>i:
			pos = i+(start*(start+1))/2
		else:
			pos = start+(i*(i+1))/2
		if mat[int(pos)] == 1 and visited[i] != 1:  #已经将start改变，0-7无法获取。
			deep_first(mat,n,visited,i,res)
		else:
			continue
	return [res,visited]

def get_start(visited):
	for i in range(len(visited)):
		if visited[i]:
			continue
		else:
			st = i
			break
	return st
	 
def broad_first(mat,start,n,visited):
	que = []
	visited[start] = 1
	que.insert(0,start)
	res = []
	while que!=[]:
		k = que.pop()
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
	return [res,visited]


def main():
	mid = [int(x) for x in input().split()]
	n_node = mid[0]
	n_edge = mid[1]
	edge = get_bian(n_edge)
	mat = build_mat(edge,n_node)
	visited_dfs = n_node*[0]
	res_dfs = []
	res_bfs = []	
	while visited_dfs!=n_node*[1]:
		start = get_start(visited_dfs)
		a =	deep_first(mat,n_node,visited_dfs,start,[])
		visited = a[1]
		res_dfs.append(a[0])
	visited_bfs = n_node*[0]
	while visited_bfs!=n_node*[1]:
		start = get_start(visited_bfs)
		q = broad_first(mat,start,n_node,visited_bfs)
		visited_bfs = q[1]
		res_bfs.append(q[0])
	for x in res_dfs:
		print('{'," ".join([str(y) for y in x ]),"}")
	for j in res_bfs:
		print('{'," ".join([str(y) for y in j ]),"}")
main()