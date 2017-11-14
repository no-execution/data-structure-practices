def main():
	info = [int(x) for x in input().split()]
	n_nodes = info[0]
	n_ways = info[1]
	ways = []
	for i in range(n_ways):
		ways.append([int(x) for x in input().split()])
	graph = [None]*n_nodes
	for x in ways:
		if graph[x[0]] == None:
			graph[x[0]] = [x[1:]]
		else:
			graph[x[0]].append(x[1:])
	que = []
	in_degree = [0]*n_nodes
	for i in range(n_nodes):
		if not graph[i]:
			continue
		for x in graph[i]:
			in_degree[x[0]] += 1
	for i in range(n_nodes):
		if in_degree[i]==0:
			que.insert(0,i)
	count = 0
	time = [0]*n_nodes
	path = []
	while que != []:
		count += 1
		mid = que.pop()
		path.append(mid)
		if graph[mid] == None:
			continue
		for x in graph[mid]:
			in_degree[x[0]] -= 1
			time[x[0]] = max(time[mid]+x[1],time[x[0]])
			if in_degree[x[0]] == 0:
				que.insert(0,x[0])
	if count != n_nodes:
		print('Impossible')
	else:
		print(max(time))
main()
