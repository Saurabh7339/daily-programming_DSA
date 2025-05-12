nums = [-1,0,1,2,-1,-4]
nums.sort()
result = []

for i in range(len(nums)-2):
	if i>0 and nums[i+1] == nums[i-1]:
		continue

	left,right = i+1, len(nums)-1

	while left<right:
		total_sum = nums[left]+nums[right]+nums[i]
		if total_sum ==0:
			result.append([nums[left],nums[right],nums[i]])

			while left<right and nums[left]==nums[left+1]:
				left+=1
			while left<right and nums[right]==nums[right-1]:
				right-=1

			left+=1
			right-=1
		
		elif total_sum>0:
			left+=1
		else:
			right-=1
print(result)