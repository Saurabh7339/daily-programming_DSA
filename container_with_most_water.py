class Solution:
    def maxArea(self, height: list[int]) -> int:
        left =0  
        right = len(height)-1
        final_area = float('-inf')
        while left<right:
            width = right-left
            current_height = min(height[left],height[right])
            current_max = width*current_height
            if current_max>final_area:
                final_area = current_max
            
            if (height[left] > height[right]):
                right-=1
            else:
                left+=1
        return final_area



sol  =Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))    