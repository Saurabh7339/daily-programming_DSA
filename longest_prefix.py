class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        final_str = ""
        str1=strs[0]
        str2 =strs[len(strs)-1]
        for i in range(min(len(strs[0]),len(strs[len(strs)-1]))):
            if str1[i] == str2[i]:
                final_str = final_str+str1[i]
            else:
                break
        return final_str