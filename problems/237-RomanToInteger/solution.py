class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev = [1]
        res = []
        cur = []
        for i in range(numRows):
            for j in range(i+1):
                if j == i or j == 0:
                    cur.append(1)
                else:
                    cur.append(prev[j-1] + prev[j])
            res.append(cur)
            prev = cur
            cur = []
        return res