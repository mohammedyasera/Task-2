def can_see_stage(matrix):
    zipped_rows = zip(*matrix)
    transpose_matrix = [list(row) for row in zipped_rows]
    for i in transpose_matrix:
        for j in range(2):
            if i[j] > i[j+1]:
                return False
    return True

print(can_see_stage([
[2, 0, 0],
[1, 1, 1],
[2, 2, 2]
]))