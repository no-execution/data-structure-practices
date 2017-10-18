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
	print(start)
	print(visited)
	for i in range(n):
		if start>i:
			pos = i+(start*(start+1))/2
		else:
			pos = start+(i*(i+1))/2
		if mat[int(pos)] == 1 and visited[i] != 1:  #已经将start改变，0-7无法获取。
			deep_first(mat,n,visited,i,res)
		else:
			continue
	return res
def broad_first():
	pass

def main():
	mid = [int(x) for x in input().split()]
	n_node = mid[0]
	n_edge = mid[1]
	edge = get_bian(n_edge)
	mat = build_mat(edge,n_node)
	visited = n_node*[0]
	a = deep_first(mat,n_node,visited,0,[])
	print(a)
main()