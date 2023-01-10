def solve(board):
  # Find an empty cell
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        # Try filling the empty cell with a number
        for k in range(1, 10):
          if isValid(board, i, j, k):
            board[i][j] = k
            # Recursively try to solve the rest of the puzzle
            if solve(board):
              return True
            # If the solution doesn't work, reset the cell to empty and try again
            board[i][j] = 0
        # If none of the numbers work, return False to trigger backtracking
        return False
  # If the board is full, it must be solved
  return True

def isValid(board, row, col, num):
  # Check if the number is already in the row
  for i in range(9):
    if board[row][i] == num:
      return False
  # Check if the number is already in the column
  for i in range(9):
    if board[i][col] == num:
      return False
  # Check if the number is already in the 3x3 box
  startRow = row - row % 3
  startCol = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[startRow + i][startCol + j] == num:
        return False
  # If the number is not already in the row, column, or box, it is valid
  return True

# Example usage:
board = [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7]
]

if solve(board):
  print(board)
else:
  print("Unable to solve the puzzle.")