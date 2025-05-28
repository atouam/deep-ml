def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = [[] for _ in range(len(a[0]))]
    for row in b :
        for line in a :
            row.append(line.pop(0))
	return b