from collections import defaultdict
def isValidSudoku(board):
    # Definition of the Hashmap to keep track of the values
    rows = defaultdict(set)
    cols = defaultdict(set)
    block = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue

            if (
                board[i][j] in rows[i] or
                board[i][j] in cols[j] or
                board[i][j] in block[(i // 3,j // 3)]
            ):
                return False

            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            block[(i // 3,j // 3)].add(board[i][j])
    
    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))