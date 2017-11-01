def get_linjie(n):
	res = []
	for i in range(n):
		res.append([int(x) for x in input().split()])
	return res

def get_pos(a,b):
	if a>=b:
		return int(b+a*(a+1)/2)
	else:
		return int(a+b*(b+1)/2)

#把输入的所有编号都减一了。输出时记得加一。
def build_linjie(n,nodes):
	mat = int(n*(n+1)/2)*[444]
	for i in range(n):
		mat[int(i+i*(i+1)/2)] = 0
	for x in nodes:
		if x[0]<x[1]:
			pos = int((x[0]-1)+(x[1]-1)*x[1]/2)
		elif x[0]>x[1]:
			pos = int((x[1]-1)+(x[0]-1)*x[0]/2)
		mat[pos] = x[2]
	return mat

def floyd(n,mat):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				pos = get_pos(i,j)
				a = mat[get_pos(i,k)]+mat[get_pos(k,j)]
				b = mat[get_pos(i,j)]
				if a<b:
					mat[pos] = a
	return mat	

#每次判断一个点
def get_minmax(tar,n,mat):
	res = 0
	for i in range(n):
		pos = get_pos(tar,i)
		if mat[pos]==444:
			return False
		if mat[pos]>res:
			res = mat[pos]
	return res


def main():
	q = [int(x) for x in input().split()]
	n_animals = q[0]
	n_linjie = q[1]
	a = get_linjie(n_linjie)
	mat = build_linjie(n_animals,a)
	mid = floyd(n_animals,mat)
	res = 444
	k = -1
	for i in range(n_animals):
		b = get_minmax(i,n_animals,mid)
		if not b:
			continue
		if b<res:
			res = b
			k = i
	if res == 444:
		print('0')
	else:
		print(" ".join([str(k+1),str(res)]))		
main()