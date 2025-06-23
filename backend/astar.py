# backend/astar.py

import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_path_finding(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0 + heuristic(start, end), 0, start, [])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        path = path + [current]
        if current == end:
            return path

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    heapq.heappush(open_set, (
                        g + 1 + heuristic(neighbor, end), g + 1, neighbor, path
                    ))

    return []
