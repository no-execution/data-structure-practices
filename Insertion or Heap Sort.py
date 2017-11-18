def insertion_sort(nums,mid):
	n_nums = len(nums)
	flag = False
	for i in range(1,n_nums):
		tmp = nums[i]
		count = i
		while count>0:
			if nums[count-1]>tmp:
				nums[count] = nums[count-1]
				count -= 1
			else:
				break
		nums[count] = tmp
		if flag:
			next_iteration = nums
			break
		if mid == nums:
			flag = True
	if flag:
		return next_iteration
	else:
		return False



def heap_pass(nums):
	n = len(nums)-1
	while True:
		k = nums[:]
		nums = adjust_heap(nums,n)
		if k==nums:
			break
	return nums

def adjust_heap(nums,n):
	i = 0
	while i*2+1!=n and i*2+2!=n:    #最后一个非叶节点的判断依据
		i+=1
	while i>=0:
		#对当前节点(非叶节点)进行调整
		if 2*i+1 == n:   #单儿子
			if nums[2*i+1] > nums[i]:
				tmp = nums[2*i+1]
				nums[2*i+1] = nums[i]
				nums[i] = tmp
		elif 2*i+2 <= n:   #双儿子
			max_val = max(nums[2*i+1],nums[2*i+2])
			if max_val > nums[i]:
				if max_val == nums[2*i+1]:
					nums[2*i+1] = nums[i]
					nums[i] = max_val
				else:
					nums[2*i+2] = nums[i]
					nums[i] = max_val
		i -=1
	return nums

def delete_max(nums,size):   #size代表队尾的位置
	tmp = nums[0]
	nums[0] = nums[size]
	x = nums[size]
	nums[size] = tmp
	size -= 1
	k = 0
	while 2*k+1<=size:
		child = 2*k+1
		if child!=size and nums[child]<nums[child+1]:
			child += 1
		if nums[k] >= nums[child]:
			break
		else:
			mid = nums[k]
			nums[k] = nums[child]
			nums[child] = mid
			k = child
	nums[k] = x
	return nums

def heap_sort(nums,mid):
	size = len(nums) - 1
	nums = heap_pass(nums)
	flag = False
	while size > 0:
		nums = delete_max(nums,size)
		size -= 1
		if flag:
			next_iteration = nums[:]
			break
		if nums == mid:
			flag = True
	if flag:
		return next_iteration
	else:
		return False

def main():
	n_nums = int(input())
	nums = [int(x) for x in input().split()]
	mid = [int(x) for x in input().split()]
	nums_other = nums[:]
	mid_other = mid[:]
	a = insertion_sort(nums,mid)
	if a:
		print('Insertion Sort')
		print(" ".join([str(x) for x in a]))
		return
	b = heap_sort(nums_other,mid_other)
	if b:
		print('Heap Sort')
		print(" ".join([str(x) for x in b]))
		return
main()