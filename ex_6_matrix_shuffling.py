def is_valid_command(comman, r, c):
    commands = comman.split(' ')
    if commands[0] == 'swap' and len(commands) == 5:
        row_1 = int(commands[1])
        col_1 = int(commands[2])
        row_2 = int(commands[3])
        col_2 = int(commands[4])
        if 0 <= row_1 < r and 0 <= row_2 < r and 0 <= col_1 < c and 0 <= col_2 < c:
            return True


rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append(input().split())

command = input()
while not command == 'END':
    if is_valid_command(command, rows, cols):
        coordinates = command.split()
        r_1 = int(coordinates[1])
        c_1 = int(coordinates[2])
        r_2 = int(coordinates[3])
        c_2 = int(coordinates[4])
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        for row in matrix:
            print(' '.join(row))

    else:
        print('Invalid input!')

    command = input()




