import random

grid = [[0 for _ in range(9)] for _ in range(9)]

cn_numbers = "零一二三四五六七八九"

def is_valid_move(row, col, num):
    # Check if the number is not in the current row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check if the number is not in the current column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if the number is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def find_empty_location():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def fill_board():
    empty_location = find_empty_location()
    if not empty_location:
        return True  # Puzzle is solved

    row, col = empty_location
    numbers = list(range(1, 10))
    random.shuffle(numbers)  # Randomize the order of numbers

    for num in numbers:
        if is_valid_move(row, col, num):
            grid[row][col] = num
            if fill_board():
                return True
            grid[row][col] = 0  # Backtrack

    return False  # Trigger backtracking


def print_grid():
    for row in grid:
        print(*map(cn_numbers.__getitem__, row), sep='')

def generate_puzzle():
    fill_board()
    # Remove some numbers to create a puzzle
    attempts = 30  # Number of cells to clear
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:  # Only remove if the cell is not already empty
            grid[row][col] = 0
            attempts -= 1

    print_grid()


if __name__ == "__main__":
    generate_puzzle()
    print("Puzzle generated successfully!")




