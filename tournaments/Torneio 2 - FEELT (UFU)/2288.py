# 2288 - Tv da Vovó
# BALSAQUE
test = 1
while True:
	lines, columns = map(int,input().split())
	if not lines and not columns:
		break

	matrix = []
	for _ in range(lines):
		matrix.append(list(map(int,input().split())))

	hor = 0
	ver = 0
	while True:
		newHor, newVer = map(int,input().split())
		if not newHor and not newVer:
			break
		hor += newHor
		ver += newVer
	hor %= columns
	ver %= lines

	if ver:
		matrix = matrix[ver:] + matrix[:ver]
	if hor:
		for i in range(len(matrix)):
			matrix[i] = matrix[i][-hor:] + matrix[i][:-hor]

	print("Teste " + str(test))
	test += 1
	for line in matrix:
		print(" ".join(map(str,line)))

	print()
