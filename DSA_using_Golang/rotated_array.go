package main

func rotated(nums []int, k int) []int {

	for i := range k {
		i = 0
		var temp = nums[i]
		for j := range len(nums) - 1 {
			nums[j] = nums[j+1]
		}
		nums[len(nums)-1] = temp
	}
	return nums
}
