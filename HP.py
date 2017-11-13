def get_pos(a,b):
	if a>=b:
		return int(b+a*(a+1)/2)
	else:
		return int(a+b*(b+1)/2)

def get_minmax(tar,n,mat):
	res = 0
	for i in range(n):
		pos = get_pos(tar,i)
		if mat[pos]==101:
			return False
		if mat[pos]>res:
			res = mat[pos]
	return res

def main():
	q = [int(x) for x in input().split()]
	n_animals = q[0]
	n_linjie = q[1]
	info = []
	for i in range(n_linjie):
		info.append([int(x) for x in input().split()])
	mat = int(n_animals*(n_animals+1)/2)*[101]
	for i in range(n_animals):
		mat[int(i+i*(i+1)/2)] = 0
	for x in info:
		pos = get_pos(x[0]-1,x[1]-1)
		mat[pos] = x[2]
	for k in range(n_animals):
		for i in range(n_animals):
			for j in range(n_animals):
				if i==j or i==k or j==k:
					continue
				pos = get_pos(i,j)
				a = mat[get_pos(i,k)]+mat[get_pos(k,j)]
				b = mat[get_pos(i,j)]
				if a<b:
					mat[pos] = a
	res = 101
	k = -1
	for i in range(n_animals):
		b = get_minmax(i,n_animals,mat)
		if not b:
			continue
		if b<res:
			res = b
			k = i
	if res == 101:
		print('0')
	else:
		print(k+1,res)	
			
main()