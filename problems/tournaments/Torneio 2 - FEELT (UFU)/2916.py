# # 2916 - The Note
mod = 1000000007
while True:
    try:
        entry = input().split()
        N = int(entry[0])

        # handling inputs in multiple lines (same behavior as scanf / cin)
        while len(entry) <= N + 1:
            entry += input().split()

        K = int(entry[1])
        notas = list(map(int, entry[2:]))
    except EOFError:
        break

    notas.sort(reverse=True)
    soma = 0
    for i in range(K):
        soma += notas[i]
    print(soma % mod)
