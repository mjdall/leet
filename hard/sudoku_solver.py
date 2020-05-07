NUMS = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
    
def convert_to_solution(self, board):
    new_board = [['' for _ in range(0, 9)] for _ in range(0, 9)]
    
    for y_idx, row in enumerate(board):
        for x_idx, entry in enumerate(row):
            new_board[y_idx][x_idx] = str(entry)
        
    return new_board

def get_x_y_lookup(self, board):
    x_board = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
    y_board = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
    start_index = None
    
    for y_idx, row in enumerate(board):
        for x_idx, entry in enumerate(row):
            if entry == '.':
                if start_index is None:
                    start_index = (x_idx, y_idx)
                continue
            x_board[y_idx][x_idx] = int(entry)
            y_board[x_idx][y_idx] = int(entry)
    
    return x_board, y_board, start_index

def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    x_board, y_board, start_index = self.get_x_y_lookup(board)
    
    if start_index is None:
        return self.convert_to_solution(x_board)
    
    solution = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
    self.backtrack(solution, x_board, y_board, *start_index)

    solution = self.convert_to_solution(solution)
    
    return solution

def get_new_x_y(self, x_idx, y_idx):
    x_idx += 1
    if x_idx == 9:
        x_idx = 0
        y_idx += 1

    return x_idx, y_idx

def backtrack(self, solution_board, x_board, y_board, x_idx, y_idx):
    if solution_board[0][0] != 0:
        return()
    
    non_zero_entry = x_board[y_idx][x_idx] != 0
    at_final_idx = x_idx == 8 and y_idx == 8
    
    if non_zero_entry and at_final_idx:
        solution_board = x_board
        print(x_board)
        return()

    new_x, new_y = self.get_new_x_y(x_idx, y_idx)
    
    if non_zero_entry:
        self.backtrack(solution_board, x_board[:], y_board[:], new_x, new_y)
        return()
    
    row = x_board[y_idx]
    col = y_board[x_idx]
    
    numbers_in_row = set(row + col)
    if 0 in numbers_in_row:
        numbers_in_row.remove(0)
    
    possible_nums = self.NUMS.difference(numbers_in_row)

    if not possible_nums:
        return()

    for num in possible_nums:
        if at_final_idx:
            x_board[y_idx][x_idx] = num
            solution_board = x_board
            return()

        x_board_copy = x_board[:]
        y_board_copy = y_board[:]
        
        x_board_copy[y_idx][x_idx] = num
        y_board_copy[x_idx][y_idx] = num
        
        self.backtrack(solution_board, x_board_copy, y_board_copy, new_x, new_y)
