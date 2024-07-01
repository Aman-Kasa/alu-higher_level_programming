#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_size_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)

if len(sys.argv) != 2:
    print_usage_and_exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print_number_error_and_exit()

if N < 4:
    print_size_error_and_exit()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0

    return res

def solve():
    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    solve()
