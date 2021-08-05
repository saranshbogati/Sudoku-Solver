board = [
    [5,0,0,0,0,0,4,2,0],
    [0,0,2,6,8,0,9,0,5],
    [0,0,7,0,5,0,0,8,0],
    [0,8,5,4,0,9,1,0,0],
    [7,0,4,0,0,2,0,9,8],
    [2,1,0,0,3,0,0,0,4],
    [4,7,0,8,0,1,2,0,0],
    [0,0,1,0,0,0,3,4,0],
    [0,2,0,3,0,5,8,7,0],
]

def find_empty_square(board):
    for i in range(9): # loop through 9 rows
        for j in range(9): # loop through all cols in the row
            if board[i][j] == 0:
                return i, j 
    return None # return none if no empty square are found 

def is_valid(board, value, row, col):
    # check if values conflict with rows
    if value in board[row]:
        return False
    
    col_list = []
    for i in range(9):
        col_list.append(board[i][col])
    if value in col_list:
        return False

    # check for value 3*3 block
    row_block_start = ( row // 3 ) * 3 # eg  4 // 3 = 1 so start of row is 1 * 3  = 3
    col_block_start = ( col // 3 ) * 3 # eg  2 // 3 = 0 so start of col is 0 * 3  = 0

    for i in range(row_block_start, row_block_start + 3 ): # eg. 3 to 6
        for j in range(col_block_start, col_block_start + 3 ):
            if board[i][j] == value:
                return False
    return True 



def solve_sudoku():
    try:
        find_result = find_empty_square(board)

        if find_result is None:
            print(board)
            return True # if no empty square is found we have solved the sudoku 
        
        row, col = find_result

        for i in range(1,10):
            is_value_ok = is_valid(board, i,row, col)
            if is_value_ok:
                board[row][col] = i

                # if while solving sudoku we get true exit out since we solved it 
                if solve_sudoku(): 
                    return True

                # else set the previous set value to 0 to check for other values
                board[row][col] = 0 
    except Exception as e:
        print(e)

if __name__ == "__main__":
    solve_sudoku()

