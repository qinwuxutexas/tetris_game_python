# Set up the board.
# The board is represented as an array of arrays, with 10 rows and 10 columns.
board_size = { "x": 10, "y": 10 }
board = [[0] * board_size["x"] for _ in range(board_size["y"])]

# Draws the contents of the board with a border around it.
def draw_board():
    board_border = "".join(["*" for _ in range(board_size["x"] + 2)])
    print(board_border)
    for y in range(board_size["y"]):
        line = "|"
        for x in range(board_size["x"]):
            line += ("#" if board[y][x] else " ")
        line += "|"
        print(line)
    print(board_border)
