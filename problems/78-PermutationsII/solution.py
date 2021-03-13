from collections import deque, defaultdict

q = deque()
res = set()
seen = defaultdict(lambda:False)

def bfs(cur_perm, elem):
    key = "".join([str(x) for x in cur_perm]) +str(elem)
    if seen[key]:
        return 
    for i in range(len(cur_perm)):
        new_perm = cur_perm[ :i] +[elem]+ cur_perm[i:]
        if tuple(new_perm) not in res:
            res.add(tuple(new_perm))
            q.append(new_perm)
    seen[key] = True

def permuteUnique(nums):
    q.append(nums)
    while q:
        seq = q.popleft()
        for idx, elem in enumerate(seq):
            cur_perm = seq[:idx]+seq[idx+1:]
            bfs(cur_perm, elem)     
    return list(res)
    
print(permuteUnique([1,2,3]))
    