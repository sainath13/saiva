import random
from collections import deque

GRID_ROWS = 6
GRID_COLS = 9

def create_empty_grid():
    return [['.' for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def place_entities(grid, difficulty):
    # Place Player and AntiPlayer
    while True:
        player_row = random.randint(0, GRID_ROWS-1)
        player_col = random.randint(0, GRID_COLS-1)
        anti_row = random.randint(0, GRID_ROWS-1)
        anti_col = random.randint(0, GRID_COLS-1)
        
        if (player_row, player_col) != (anti_row, anti_col):
            grid[player_row][player_col] = 'Player'
            grid[anti_row][anti_col] = 'AntiPlayer'
            break

    # Place Checkpoints
    while True:
        player_chk_row = random.randint(0, GRID_ROWS-1)
        player_chk_col = random.randint(0, GRID_COLS-1)
        anti_chk_row = random.randint(0, GRID_ROWS-1)
        anti_chk_col = random.randint(0, GRID_COLS-1)
        
        if (player_chk_row, player_chk_col) != (anti_chk_row, anti_chk_col) and \
           (player_chk_row, player_chk_col) != (player_row, player_col) and \
           (anti_chk_row, anti_chk_col) != (anti_row, anti_col):
            grid[player_chk_row][player_chk_col] = 'PlayerCheckpoint'
            grid[anti_chk_row][anti_chk_col] = 'AntiPlayerCheckpoint'
            break

    # Add Blocks and Barrels based on difficulty
    max_blocks = min(15, 3 + difficulty * 3)
    max_barrels = min(5, 1 + difficulty)
    
    for _ in range(random.randint(3, max_blocks)):
        while True:
            row = random.randint(0, GRID_ROWS-1)
            col = random.randint(0, GRID_COLS-1)
            if grid[row][col] == '.':
                grid[row][col] = 'Block'
                break

    for _ in range(random.randint(1, max_barrels)):
        while True:
            row = random.randint(0, GRID_ROWS-1)
            col = random.randint(0, GRID_COLS-1)
            if grid[row][col] == '.':
                grid[row][col] = 'Barrel'
                break

    return grid

def is_solvable(grid):
    # Find positions
    player = anti = p_chk = a_chk = None
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            if grid[i][j] == 'Player': player = (i, j)
            if grid[i][j] == 'AntiPlayer': anti = (i, j)
            if grid[i][j] == 'PlayerCheckpoint': p_chk = (i, j)
            if grid[i][j] == 'AntiPlayerCheckpoint': a_chk = (i, j)
    
    if None in [player, anti, p_chk, a_chk]:
        return False

    # BFS Solver
    queue = deque([(player, anti, [])])
    visited = set((player, anti))
    
    while queue:
        p_pos, a_pos, path = queue.popleft()
        
        if p_pos == p_chk and a_pos == a_chk:
            return True
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            # Player move
            new_p = (p_pos[0] + dx, p_pos[1] + dy)
            if not (0 <= new_p[0] < GRID_ROWS and 0 <= new_p[1] < GRID_COLS) or \
               grid[new_p[0]][new_p[1]] in ['Block', 'Barrel']:
                new_p = p_pos
            
            # Antiplayer move
            new_a = (a_pos[0] - dx, a_pos[1] - dy)
            if not (0 <= new_a[0] < GRID_ROWS and 0 <= new_a[1] < GRID_COLS) or \
               grid[new_a[0]][new_a[1]] in ['Block', 'Barrel']:
                new_a = a_pos
            
            # Collision check
            if new_p == new_a:
                continue
                
            if (new_p, new_a) not in visited:
                visited.add((new_p, new_a))
                queue.append((new_p, new_a, path + [(dx, dy)]))
    
    return False

def generate_level(difficulty=2, max_attempts=100):
    for _ in range(max_attempts):
        grid = create_empty_grid()
        grid = place_entities(grid, difficulty)
        
        # Make a deep copy for validation
        test_grid = [row.copy() for row in grid]
        if is_solvable(test_grid):
            # Format the output
            formatted = []
            for row in grid:
                formatted_row = []
                for cell in row:
                    if cell in ['Player', 'AntiPlayer']:
                        formatted_row.append(cell)
                    elif cell in ['PlayerCheckpoint', 'AntiPlayerCheckpoint']:
                        formatted_row.append(cell)
                    else:
                        formatted_row.append(cell if cell in ['Block', 'Barrel'] else '.')
                formatted.append(formatted_row)
            return formatted
    return None

# Generate and print a level
level = generate_level(difficulty=2)
if level:
    for row in level:
        print(str(row).replace("'", '"') if row[0] != '.' else str(row))
else:
    print("Failed to generate valid level")
