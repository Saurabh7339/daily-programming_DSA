import math

def findMedianSortedArrays(nums1, nums2):
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    total_len = nums1_len+nums2_len
    final_index = None
    result = None
    if total_len%2!=0:
        print("hey testing for odd here")
        index = math.floor(total_len/2)
        if index>=len(nums1):
            next_array_index = len(nums2)-(len(nums1)+1)
            final_index = next_array_index
            result = nums2[final_index]
        else:
            final_index = index
            result = nums2[final_index]
    else:
        print("hey testing here")
        index = math.floor(total_len/2)
        print(index)
        if index==len(nums1):
            print("edge case")
            total_summed_value = (nums1[nums1_len-1] + nums2[0]) /2
            result = total_summed_value 
        elif index>len(nums1):
            print("not an edge case")
            next_array_index = len(nums2)-(len(nums1)+1)
            print(next_array_index)
            total_summed_value = (nums2[next_array_index] + nums2[next_array_index+1]) /2 
            result = total_summed_value
        
    return result


nums1 = [1,3]
nums2 =[2]

print(findMedianSortedArrays(nums1,nums2))