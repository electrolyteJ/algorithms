def print_board(board):
    if not board or not board[0]:return []
    m = len(board)
    n = len(board[0])
    lines = ''
    print('\n')
    for i in range(m):
        for j in range(n):
            if j == 0:
                lines += '['
            lines += str(board[i][j])
            if j == n-1:
                lines +=']'
                lines += '\n'
            else:
                lines +='\t'
    print(lines)
