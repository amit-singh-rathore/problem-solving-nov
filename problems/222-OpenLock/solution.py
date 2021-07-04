class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends: 
            return -1
        
        next_slot = { str(i) : [str(i+1), str(i-1)] for i in range(1, 9)}
        next_slot["0"] = ["1", "9"]
        next_slot["9"] = ["0", "8"]
        
        queue = collections.deque([('0000', 0)])
        
        deadends = set(deadends)
        deadends.add("0000")
        while queue:
            cur_comb, turns = queue.popleft()
            if cur_comb == target: 
                return turns
            for i in range(4):
                for ns in next_slot[cur_comb[i]]:
                    new_comb = cur_comb[:i] + ns + cur_comb[i+1:]
                    if new_comb not in deadends:
                        deadends.add(new_comb)
                        queue += (new_comb, turns + 1),
        return -1