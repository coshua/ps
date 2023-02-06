class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        keys = rooms[0]
        visited = [0] * len(rooms)
        visited[0] = 1

        while keys:
            nxt = keys.pop()
            if not visited[nxt]:
                for nxtkey in rooms[nxt]:
                    if not visited[nxtkey]:
                        keys.append(nxtkey)
                visited[nxt] = 1

        return True if sum(visited) == len(rooms) else False