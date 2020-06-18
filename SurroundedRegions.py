# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border,
# which means that any 'O' on the border of the board are not flipped to 'X'.
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.
import collections


def surrounded_regions(board):
    def get_first_index_eq_0(graph):
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 0:
                    return [i, j]
        return [-1, -1]

    if board == []:
        return []
    graph = [[1 for i in range(len(board[0]))] for j in range(len(board))]
    column = len(graph[0])
    row = len(graph)
    for i in range(row):
        for j in range(column):
            # print(i, j)
            if board[i][j] == 'O':
                graph[i][j] = 0
    indexes = get_first_index_eq_0(graph)
    more = not indexes == [-1, -1]
    while more:
        q = collections.deque()
        q.append(indexes)
        result_arr = []
        surrounded = True
        while q:
            i, j = q.popleft()
            # print(i, j)
            graph[i][j] = 1
            result_arr.append([i, j])
            if i in [0, row - 1] or j in [0, column - 1]:
                surrounded = False
            for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                x, y = i + dx, j + dy
                if 0 <= x < row and 0 <= y < column and graph[x][y] == 0:
                    q.append([x, y])
                    graph[x][y] = 1
        if surrounded:
            for i, j in result_arr:
                board[i][j] = 'X'
        indexes = get_first_index_eq_0(graph)
        more = not indexes == [-1, -1]
    return board


b = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
     ["O", "X", "O", "X", "O", "X"]]

for r in surrounded_regions(b):
    print(r)
