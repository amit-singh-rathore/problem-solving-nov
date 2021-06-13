class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_distnace(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + \
                   (p1[1] - p2[1]) * (p1[1] - p2[1])
        
        d=[
            get_distnace(p1,p2),
            get_distnace(p1,p3),
            get_distnace(p1,p4),
            get_distnace(p2,p3),
            get_distnace(p2,p4),
            get_distnace(p3,p4)
        ]
        d.sort()
        
        return  (all(x == d[0] for x in d[0:4]) and
                 d[4] > d[3] and d[4]==d[5])