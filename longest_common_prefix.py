class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for i in arr1:
            strng = ""
            for j in str(i):
                strng+=j
                s.add(strng)
        max_length= 0
        for i in arr2:
            strng =""
            for j in str(i):
                strng+=j
                if strng in s:
                    store_len = len(strng)
                    if store_len>max_length:
                        max_length= store_len
        return max_length
                

        