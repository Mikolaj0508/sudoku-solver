from main import sudoku
from visual import print_board
from random import randrange

'''
How board to play looks like
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
'''

number_of_test = input("Enter number of test (it has to be integer): ")

try:
  for test in range(int(number_of_test)):
    print(f"\n Test number {test}")
    board_to_test= [[randrange(start=0,stop=9) for _ in range(9)] for _ in range(9)]
    print_board(board_to_test)
    sudoku(board_to_test)
    print(f"{'-'*20}")
    print_board(board_to_test)
except (TypeError,ValueError):
  print("Cannot be interpreted as an integer")

