def main():
    from sys import stdin, stdout
    from operator import itemgetter

    while True:
        p, a, r = map(int, stdin.readline().split())
        if p == a == r == 0:
            break

        # Hash-table: muito rapida, facil de gerar um array ordenado
        perolas = {stdin.readline().strip(): 0 for _ in range(p)}
        alunos = {}

        for _ in range(a):
            aluno = stdin.readline().strip()
            #  Aluno pode existir em alunos e ter um valor muito melhor.
            #  Criando tmp, so alteramos o valor de alunos[aluno]
            #  se for aumentar a quantidade de perolas daquele aluno
            tmp = 0
            for _ in range(r):
                resposta = stdin.readline().strip()
                # Decrementar facilita sorted(), podemos ordenar crescentemente
                # e continuar com os maiores valores no comeco
                # (N ha valores verdadeiramente negativos no dict)
                if resposta in perolas:
                    tmp -= 1

            # Se for um aluno novo ou for repetido com maior nota
            if aluno not in alunos or tmp < alunos[aluno]:
                alunos[aluno] = tmp

        # itemgetter: mais rapido, 1 eh o value, 0 eh a key
        final = sorted(alunos.items(), key=itemgetter(1, 0))

        ans = prev_nome = final[0][0]
        prev_perolas = final[0][1]
        # print(*final)  # debug
        for i in range(1, len(final)):
            if final[i][1] == prev_perolas:
                # Nao imprima se o nome e qtde de perolas
                # forem iguais ao aluno anterior
                if final[i][0] == prev_nome:
                    continue
                prev_nome = final[i][0]
                ans += ', ' + prev_nome
            else:
                break
        stdout.write('%s\n' % ans)

main()
