sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]


for i in range(len(sudoku)):
        if i % 3 == 0:
            print("- "*12)
            for j in range(len(sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(sudoku[i][j])
                else:
                    print(str(sudoku[i][j]) + " ", end="")
        if i % 3 == 1:
            for j in range(len(sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(sudoku[i][j])
                else:
                    print(str(sudoku[i][j]) + " ", end="")

        if i % 3 == 2:
            for j in range(len(sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(sudoku[i][j])
                else:
                    print(str(sudoku[i][j]) + " ", end="")


print("- "*12)
