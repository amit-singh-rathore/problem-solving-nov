class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        counter = Counter(candidates)
        keys = list(counter.keys())
        
        def helper(combo, curr, total):
            if total == target:
                ans.append(combo)
            elif total > target:
                combo.pop()
            else:
                for i in range(curr, len(keys)):
                    k = keys[i]
                    if counter[k] > 0:
                        counter[k] -= 1
                        helper(combo+[k], i, total+k)
                        counter[k] += 1

        
        for i in range(len(keys)):
            k = keys[i]
            counter[k] -= 1
            helper([k], i, k)
        return ans
        
        
        
                
    
