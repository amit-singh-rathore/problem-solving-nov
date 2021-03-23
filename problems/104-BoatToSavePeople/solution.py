class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l_idx, h_idx = 0, len(people) - 1
        ans = 0
        while l_idx <= h_idx:
            ans += 1
            if people[l_idx] + people[h_idx] <= limit:
                l_idx += 1
            h_idx -= 1
        return ans
        