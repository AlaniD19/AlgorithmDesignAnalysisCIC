def bfs_maze(maze, R, C, Sr, Sc, Tr, Tc, O):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_letters = ['U', 'R', 'D', 'L']
    queue = [(Sr, Sc)]
    visited = [[False] * C for _ in range(R)]
    visited[Sr][Sc] = True
    prev = [[None] * C for _ in range(R)]
    dist = [[0] * C for _ in range(R)]

    while queue:
        r, c = queue.pop(0)
        if r == Tr and c == Tc:
            if O == 1:
                return "True"
            elif O == 2:
                return dist[r][c]
            elif O == 3:
                path = []
                while (r, c) != (Sr, Sc):
                    pr, pc = prev[r][c]
                    for i, (dr, dc) in enumerate(directions):
                        if (pr, pc) == (r - dr, c - dc):
                            path.append(direction_letters[i])
                            break
                    r, c = pr, pc
                return ''.join(reversed(path))

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and maze[nr][nc] == ' ':
                queue.append((nr, nc))
                visited[nr][nc] = True
                prev[nr][nc] = (r, c)
                dist[nr][nc] = dist[r][c] + 1

    if O == 1:
        return "False"
    elif O == 2:
        return -1
    elif O == 3:
        return ""


if __name__ == "__main__":
    R, C, Sr, Sc, Tr, Tc, O = map(int, input().split())
    maze = [list(input().strip()) for _ in range(R)]
    result = bfs_maze(maze, R, C, Sr, Sc, Tr, Tc, O)
    print(result)