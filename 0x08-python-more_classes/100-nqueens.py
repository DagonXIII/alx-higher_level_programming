#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it is safe to place a queen at board[row][col]."""
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row):
    """Recursive function to solve the N-Queens problem."""
    # Base case: If all queens are placed, print the solution
    if row == N:
        print_solution(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    """Print the solution in the required format."""
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

# Check if the program is called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is greater or equal to 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [[0] * N for _ in range(N)]

# Solve the N-Queens problem
solve_n_queens(board, 0)
