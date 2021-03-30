class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        smallest = strs[0]
        l = len(smallest)
        largest = strs[-1][:l]
        i = 0
        while i<l:
            if largest[i] == smallest[i]:
                i += 1
            else:
                break
        return smallest[0:i]

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         smallest_word = min(strs, key=len)
        
#         for i in range(len(smallest_word), 0, -1):
#             prefix = smallest_word[0:i]
#             if all(s.startswith(prefix) for s in strs):
#                 return prefix
#         return ""