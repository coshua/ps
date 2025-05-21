class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = [(sr, sc)]
        
        s = image[sr][sc]
        image[sr][sc] = color
        if s == color:
            return image
        rsz = len(image)
        csz = len(image[0])
        dirs = [[-1, 0], [0,1],[0,-1],[1,0]]
        while q:
            r, c = q.pop()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rsz and 0 <= nc < csz and image[nr][nc] == s:
                    q.append((nr, nc))
                    image[nr][nc] = color
            
        
        return image