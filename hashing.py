def get_mod(n):
	while n<=2:
		return 2
	while True:
		i = 2
		mid = n**0.5
		flag = True
		while i <= mid:
			if n%i == 0:
				flag = False
				break
			else:
				i += 1
		if flag:
			break
		n += 1
	return n

#插入一个数字
def insert(x,table,mod):
	key = x%mod
	i = 1
	flag = [-1]*mod
	while table[key] != None:
		key += 2*i-1
		while key >= mod:
			key -= mod
		if flag[key] == -1:
			flag[key] = 1
		else:
			return -1
		i += 1
	table[key] = x   
	return key

def main():
	info = [int(x) for x in input().split()]
	size,n_nums = info[0],info[1]
	nums = [int(x) for x in input().split()]
	mod = get_mod(size)
	table = mod*[None]
	res = n_nums*[None]
	for i in range(n_nums):
		k = insert(nums[i],table,mod)
		if k == -1:
			res[i] = '-'
		else:
			res[i] = k
	print(" ".join([str(x) for x in res]))

main()

