def Twosum(nums,k):
	nums.sort()
	result = []
	left,right = 0,len(nums)-1
	while left<right:
		s = nums[left]+nums[right]
		if s==k:
			result.append([nums[left],nums[right]])
			while left<right and nums[left] == nums[left+1]:
				left+=1
			while left<right and nums[right] == nums[right-1]:
				right-=1
			left+=1
			right-=1
		elif s<k:
			left+=1
		else:
			right-=1

	return result

print(Twosum([1,-1,0,2,2,4,-2,3],4))
