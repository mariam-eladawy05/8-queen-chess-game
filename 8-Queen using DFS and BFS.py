import time
from collections import deque

# Check if the position is safe for a queen
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# Solve the 8-Queens problem using DFS
def solve_dfs(n):
    stack = [(-1, [])]  # Stack stores (row, board_state)
    solutions = []

    while stack:
        row, board = stack.pop()

        if row == n - 1:  # All queens placed
            solutions.append(board)
        else:
            for col in range(n):
                if is_safe(board, row + 1, col):
                    stack.append((row + 1, board + [col]))

    return solutions

# Solve the 8-Queens problem using BFS
def solve_bfs(n):
    queue = deque([(-1, [])])  # Queue stores (row, board_state)
    solutions = []

    while queue:
        row, board = queue.popleft()

        if row == n - 1:  # All queens placed
            solutions.append(board)
        else:
            for col in range(n):
                if is_safe(board, row + 1, col):
                    queue.append((row + 1, board + [col]))

    return solutions

# Display the board for a given solution
def display_board(solution):
    n = len(solution)
    for row in range(n):
        line = ["Q" if col == solution[row] else "." for col in range(n)]
        print(" ".join(line))
    print("\n")

# Main program
n = int(input('enter size of board: '))

print("Solving Queens problem using DFS...")
start_time = time.time()
dfs_solutions = solve_dfs(n)
dfs_time = time.time() - start_time
print(f"DFS found {len(dfs_solutions)} solutions in {dfs_time:.4f} seconds.\n")

print("Solving Queens problem using BFS...")
start_time = time.time()
bfs_solutions = solve_bfs(n)
bfs_time = time.time() - start_time
print(f"BFS found {len(bfs_solutions)} solutions in {bfs_time:.4f} seconds.\n")

# Display a single solution as an example
print("Example solution:")
display_board(dfs_solutions[0])

if dfs_time < bfs_time:
    print("DFS is a better algorithm for this Game!")
else:
    print("BFS is a better algorithm for this Game!")