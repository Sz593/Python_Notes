#! python3

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')
    print()

#print('\n'.join(map(''.join, zip(*grid))))


