class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        q = deque()
        q.append(0)
        while q:
            room_idx = q.popleft() 
            visited[room_idx] = True
            for key in rooms[room_idx]:
                if not visited[key]:
                    q.append(key)

        return all(visited)