class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Step 1: Sort the array
        result = []
        min_val = float('-inf')
        store = []
        closest_sum= float('inf')

        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Step 4: Check if this sum is closer to the target than the previous closest
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Step 5: Move the pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Increase the sum
                elif current_sum > target:
                    right -= 1  # Decrease the sum
                else:
                    return current_sum 

        return closest_sum
        