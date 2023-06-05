#!/usr/bin/python3

"""
N-Queens backtracking program to print the coordinates of N queens
on an N x N grid such that they are all in non-attacking positions.
"""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row):
    """Recursive function to solve the N-Queens problem"""
    if row == N:
        # Base case: All queens have been placed, print the solution
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            # Place a queen at board[row] = col
            board[row] = col

            # Recursive call to place queens in the next row
            solve_nqueens(board, row + 1)

def print_solution(board):
    """Print the solution as a list of coordinates"""
    solution = [[i, board[i]] for i in range(N)]
    print(solution)

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty list to represent the board
board = [None] * N

# Solve the N-Queens problem
solve_nqueens(board, 0)
