class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_prefix_length = float('-inf')
        for i in arr1:
            str_1 = str(i)
            for j in arr2:
                str_2 = str(j)
                prefix_len = 0
                for index in range(min(len(arr1 , arr2))):
                    if str_1[index] == str_2[index]:
                        prefix_len = prefix_len+1
                if prefix_len>max_prefix_length:
                    max_prefix_length=prefix_len
        return max_prefix_length

        