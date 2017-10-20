def get_position(n):
	res = []
	for i in range(n):
		res.append([int(x) for x in input().split()])
	return res


def main():
	k = [int(x) for x in input().split()]
	n_node = k[0]
	distance = k[1]
	a = get_position(n_node)
	return a

a = main()