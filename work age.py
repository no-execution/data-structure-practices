def main():
	n_worker = int(input())
	ages = [int(x) for x in input().split()]
	res = [0]*51
	for x in ages:
		res[x] += 1
	for i in range(51):
		if res[i] != 0:
			print(str(i)+':'+str(res[i]))
main()