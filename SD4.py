def is_safe(board, row, col, num):
    # Check if 'num' is not in the given row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if 'num' is not in the given column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if 'num' is not in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num  # Tentatively place num

            if solve_sudoku(board):
                return True  # If this placement leads to a solution, return True

            board[row][col] = 0  # If not, undo the placement and backtrack

    return False  # Trigger backtracking

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the row, col of the first empty location
    return None

def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def main():
    # Sample Sudoku puzzle (0 represents an empty cell)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku:")
    print_sudoku(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_sudoku(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
