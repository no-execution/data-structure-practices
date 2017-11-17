def paopao_sort():
	n_nums = int(input())
	nums = [int(x) for x in input().split()]
	while n_nums>0:
		flag = 0
		for i in range(n_nums-1):
			if nums[i] > nums[i+1]:
				tmp = nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = tmp
				flag = 1
		if flag == 0:
			break
		n_nums -= 1
	print(" ".join([str(x) for x in nums]))

def insertion_sort():
	n_nums = int(input())
	nums = [int(x) for x in input().split()]
	for i in range(1,n_nums):
		print(nums) 
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
main()