def insertion_sort():
	n_nums = int(input())
	nums = [int(x) for x in input().split()]
	for i in range(1,n_nums):
		print(nums)   #题目中的every iteration是指在这一步进行iteration。
		tmp = nums[i]
		count = i
		while count>0:
			if nums[count-1]>tmp:
				nums[count] = nums[count-1]
				count -= 1
			else:
				break
		nums[count] = tmp
	print(" ".join([str(x) for x in nums]))


######
def merge(left,right,right_end,nums,temp_list):
	left_end = right - 1
	begin = left
	temp = left
	while left<=left_end and right<=right_end:
		if nums[left] <= nums[right]:
			temp_list[temp] = nums[left]
			left += 1
			temp += 1
		else:
			temp_list[temp] = nums[right]
			right += 1
			temp += 1
	if left <= left_end:
		for i in range(left,left_end+1):
			temp_list[temp] = nums[i]
			temp += 1
	if right <= right_end:
		for i in range(right,right_end+1):
			temp_list[temp] = nums[i]
			temp += 1
	nums[begin:right_end+1] = temp_list[begin:right_end+1]
	return nums

#递归调用，最小元的操作依赖于merge()函数
def Msort(nums,left,right_end,temp_list):
	if left < right_end:
		center = (right_end+left)//2
		Msort(nums,left,center,temp_list)
		Msort(nums,center+1,right_end,temp_list)
		merge(left,center+1,right_end,nums,temp_list)
	return nums

def merge_sort_recursive(nums):
	left = 0
	right_end = len(nums)-1
	temp_list = [-1]*len(nums)
	a = Msort(nums,left,right_end,temp_list)
	return a

###迭代法
#merge_pass是干嘛的:每次迭代并归一次
#!!!!!有问题
def merge_pass(nums,temp_list,length,n):
	i = 0
	while i<=n-2*length:
		merge(i,i+length,i+2*length-1,nums,temp_list)   #虽然不返回temp_list但是仍然改变temp_list
		i += 2*length
	if i+length < n:
		merge(i,i+length,n-1,nums,temp_list)
	else:
		temp_list[i:] = nums[i:]

def merge_sort_iterative(nums):
	n = len(nums)
	temp_list = [-1]*n
	length = 1
	while length<n:
		merge_pass(nums,temp_list,length,n)
		length = length*2
		print(nums)
		merge_pass(temp_list,nums,length,n)
		length = length*2
		print(nums)
	return temp_list

def main():
	n = int(input())
	if n == 1:
		num = int(input())
		print(num)
		return
	nums = [int(x) for x in input().split()]
	res = merge_sort_iterative(nums)
	print(" ".join([str(x) for x in res]))


#堆排序！！！！！！！——————————————

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

def heap_sort(nums):
	size = len(nums) - 1
	nums = heap_pass(nums)
	while size > 0:
		nums = delete_max(nums,size)
		size -= 1
		
#————————————————快速排序————————————————
#从给出的数组中找出中位数pivot,并将其放到倒数第二(第一位存最小值，最末尾存最大值)的位置
#因为对于整个快速排序，目标数组是在不断变化的，所以给出的是待排数组在整个大数组中的位置
def get_pivot(nums,left,right):
	center = (left+right)//2
	if nums[left] > nums[center]:
		tmp = nums[left]
		nums[left] = nums[center]
		nums[center] = tmp
	if nums[center] > nums[right]:
		tmp = nums[center]
		nums[center] = nums[right]
		nums[right] = tmp
	if nums[left] > nums[center]:
		tmp = nums[left]
		nums[left] = nums[center]
		nums[center] = tmp
	tmp = nums[center]
	nums[center] = nums[right-1]
	nums[right-1] = tmp
	return nums[right-1]

def quick_sort(nums,left,right):
	if (right-left) >= cutoff：    #cutoff代表使用quicksort的界限比如:超过100个数使用cutoff
		pivot = get_pivot(nums,left,right)
		low,high = left-1,right-2
		while True:
			while nums[low]
