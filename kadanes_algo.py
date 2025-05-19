def largestSumofSubArray(nums) -> int:
	max_sum = float('-inf')
	sum_temp = 0
	list_result =[]
	start_ans=0
	end_ans = 0
	for i in nums:
		if sum_temp==0:
			start=i
		sum_temp+=i
		if sum_temp<0:
			sum_temp=0
			list_result = []
		if sum_temp>max_sum:
			max_sum=sum_temp
			star_ans=start
			end_ans = i

	print(star_ans,end_ans)
	return max_sum,list_result


print(largestSumofSubArray([-2,-3,4,-1,-2,1,5,-3]))
