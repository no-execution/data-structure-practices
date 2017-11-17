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

def merge_pass(nums,temp_list,length,n):
	i = 0
	while i<=n-2*length:
		merge(i,i+length,i+2*length-1,nums,temp_list)
		i += 2*length
	if i+length < n:
		merge(i,i+length,n-1,nums,temp_list)
	else:
		temp_list[i:] = nums[i:]
	return nums

def merge_sort_iterative(nums,mid):
	n = len(nums)
	flag = False
	temp_list = [-1]*n
	length = 1
	while length<n:
		merge_pass(nums,temp_list,length,n)
		length = length*2
		if mid == nums:
			next_iteration = merge_pass(nums,temp_list,length,n)
			flag = True
			break
		merge_pass(temp_list,nums,length,n)
		length = length*2
		if mid == nums:
			next_iteration = merge_pass(nums,temp_list,length,n)
			flag = True
			break
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
	b = merge_sort_iterative(nums_other,mid_other)
	if b:
		print('Merge Sort')
		print(" ".join([str(x) for x in b]))
		return
main()