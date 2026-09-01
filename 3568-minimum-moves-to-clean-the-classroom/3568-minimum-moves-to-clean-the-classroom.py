class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = []
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        litter_id = {}
        for idx, pos in enumerate(litter):
            litter_id[pos] = idx

        target_mask = (1 << k) - 1

        
        if k == 0:
            return 0

        
        best = [[[-1] * (1 << k) for _ in range(n)]
                for _ in range(m)]

        sr, sc = start

        q = deque()
        q.append((sr, sc, 0, energy, 0))

        best[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, mask, curr_energy, moves = q.popleft()

           
            if mask == target_mask:
                return moves

            
            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

            
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                
                if classroom[nr][nc] == 'X':
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                
                if classroom[nr][nc] == 'L':
                    idx = litter_id[(nr, nc)]
                    new_mask |= (1 << idx)

                
                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1