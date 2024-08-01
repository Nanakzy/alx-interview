#!/usr/bin/python3
import sys


def is_valid(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check diagonal (upper-left)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check diagonal (upper-right)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    def solve(board, row):
        if row >= N:
            solution = [[i, j]
                        for i in range(N) for j in range(N)
                        if board[i][j] == 1]
            solutions.append(solution)
            return

        for col in range(N):
            if is_valid(board, row, col, N):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0] * N for _ in range(N)]
    solve(board, 0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
