def maxSubarraySumCircular(nums):
    temp_sum = 0
    sum_ans = float('-inf')
    index = 0
    total_count =0
    while True:
        if total_count==len(nums)+2:
            break
        if index==len(nums):
            index =0 
        temp_sum += nums[index]
        if temp_sum<0:
            temp_sum=0

        if temp_sum> sum_ans:
            sum_ans=temp_sum

        index+=1
        total_count+=1
    return total_count,sum_ans

print(maxSubarraySumCircular([5,-3,5]))