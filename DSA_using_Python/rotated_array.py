from typing import List


def rotate(nums: List[int], k: int):
        for i in range(k):
            nums = nums[1:]+nums[:1]
        return nums

nums = [1,2,3,4,5,6,7] 
k=3

nums = rotate(nums,k)
print(nums)