def count_adjacent_mines(field, i, j):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ni, nj = i + di, j + dj
            if 0 <= ni < len(field) and 0 <= nj < len(field[0]) and field[ni][nj] == '*':
                count += 1
    return count

field_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # read field
    field = []
    for i in range(n):
        row = input().strip()
        field.append(row)
    
    # process field and print output
    if field_num > 1:
        print()  # empty line between field outputs
    print(f'Field #{field_num}:')
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                print('*', end='')
            else:
                count = count_adjacent_mines(field, i, j)
                print(count, end='')
        print()  # newline after each row
    field_num += 1
