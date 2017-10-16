

#获取电脑的个数。
def nums_computers():
	return int(input())

#获取命令(并或查)。
def get_commands():
	mid = []
	while True:
		mid.append([x for x in input().split()])
		if mid[-1][0] == 'S':
			mid.pop()
			break
	return mid

#初始化并查集。
def start_sets(n):
	mid = []
	for i in range(n):
		mid.append([i+1,-1])
	return mid

#在集合中查找父元素的位置。输入的是数据的值。
def find(x,se):
	if x > len(se) or x < 1:
		return False
	k = x-1
	while True:
		if se[k][1] >= 0:
			k = se[k][1]
		else:
			break
	return k

#将两元素并起来，采用优化方法        。
def union(set_a,set_b,se):
	root_1 = find(set_a,se)
	root_2 = find(set_b,se)
	if (root_1 == root_2) and (root_1>=0):
		return False
	if se[root_2][1]>=se[root_1][1]:
		se[root_1][1] = se[root_1][1]+se[root_2][1]
		se[root_2][1] = root_1
	else:
		se[root_2][1] = se[root_2][1]+se[root_1][1]
		se[root_1][1] = root_2
	return se

#检查两个元素是否在同一集合,或者将两个集合并起来。
def execute(command,sets):
	res = []
	nums = 0
	for x in command:
		if x[0] == "C":
			res.append(bool(find(int(x[1]),sets)==find(int(x[2]),sets)))
			continue
		if x[0] == "I":
			sets = union(int(x[1]),int(x[2]),sets)
			nums = nums-1
			continue
	return [res,sets,nums]		

def main():
	n = nums_computers()
	set_all = start_sets(n)
	commands = get_commands()
	r = execute(commands,set_all)
	for x in r[0]:
		if x:
			print('yes')
		else:
			print('no')
	set_after = r[1]
	mid = n+r[2]
	if mid == 1:
		print('The network is connected.')
	else:
		print('There are',str(mid),'components.')
main()