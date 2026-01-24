def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    res = [[ sum(i * j for i, j in zip(row_a, col_b)) for col_b in zip(*b) ] for row_a in a]
    return res