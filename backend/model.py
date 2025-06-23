# backend/model.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import heapq

app = Flask(__name__)
CORS(app)  # Enable CORS

# Heuristic function for A* (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* pathfinding function
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

@app.route('/find-path', methods=['POST'])
def find_path():
    data = request.get_json()
    print("Received:", data)

    grid = data.get('grid')
    start = tuple(data.get('start'))
    end = tuple(data.get('end'))

    if not grid or not start or not end:
        return jsonify({'error': 'Invalid input'}), 400

    path = astar_path_finding(grid, start, end)
    return jsonify({'path': path})

if __name__ == '__main__':
    app.run(debug=True)
