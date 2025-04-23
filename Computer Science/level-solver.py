from collections import deque

# Define the grid
grid = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['AntiPlayer', 'Block', '.', 'Block', '.', 'Block', '.', 'Block', 'AntiPlayerCheckpoint'],
    ['Block', 'Player', 'Block', '.', 'Block', '.', 'Block', 'PlayerCheckpoint', 'Block'],
    ['Barrel', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

# Directions: right, left, down, up
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
direction_names = {(0, 1): 'right', (0, -1): 'left', (1, 0): 'down', (-1, 0): 'up'}

def find_positions(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target:
                return (i, j)
    return None

def is_valid_move(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'Block'

def bfs_solver(grid):
    player_pos = find_positions(grid, 'Player')
    antiplayer_pos = find_positions(grid, 'AntiPlayer')
    player_checkpoint = find_positions(grid, 'PlayerCheckpoint')
    antiplayer_checkpoint = find_positions(grid, 'AntiPlayerCheckpoint')

    queue = deque()
    queue.append((player_pos, antiplayer_pos, []))

    visited = set()
    visited.add((player_pos, antiplayer_pos))

    while queue:
        (player, antiplayer, path) = queue.popleft()

        if player == player_checkpoint and antiplayer == antiplayer_checkpoint:
            return path

        for dx, dy in directions:
            # Player moves in the direction (dx, dy)
            new_player_x, new_player_y = player[0] + dx, player[1] + dy
            # Antiplayer moves in the opposite direction (-dx, -dy)
            new_antiplayer_x, new_antiplayer_y = antiplayer[0] - dx, antiplayer[1] - dy

            # Check if player's move is valid
            if is_valid_move(new_player_x, new_player_y, grid):
                new_player_pos = (new_player_x, new_player_y)
            else:
                new_player_pos = player  # Player stays in place if blocked

            # Check if antiplayer's move is valid
            if is_valid_move(new_antiplayer_x, new_antiplayer_y, grid):
                new_antiplayer_pos = (new_antiplayer_x, new_antiplayer_y)
            else:
                new_antiplayer_pos = antiplayer  # Antiplayer stays in place if blocked

            # Check for collisions
            if new_player_pos == new_antiplayer_pos:
                continue  # Collision, restart

            if grid[new_player_pos[0]][new_player_pos[1]] == 'Barrel' or grid[new_antiplayer_pos[0]][new_antiplayer_pos[1]] == 'Barrel':
                continue  # Collision with barrel, restart

            # Add new state to the queue if not visited
            if (new_player_pos, new_antiplayer_pos) not in visited:
                visited.add((new_player_pos, new_antiplayer_pos))
                queue.append((new_player_pos, new_antiplayer_pos, path + [(dx, dy)]))

    return None  # No solution found

# Run the solver
solution = bfs_solver(grid)
if solution:
    # Convert the solution to arrow directions
    arrow_solution = [direction_names[move] for move in solution]
    print("Solution found! Moves:", arrow_solution)
else:
    print("No solution exists.")
