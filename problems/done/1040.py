# 1035 - Selection Test 1
def main():
    from sys import stdin, stdout

    N1, N2, N3, N4 = [float(x) for x in stdin.readline().split()]
    MEDIA = (N1*2 + N2*3 + N3*4 + N4)/10
    stdout.write("Media: %.1f\n" % MEDIA)

    if MEDIA >= 7.0:
        stdout.write("Aluno aprovado.\n")
    elif MEDIA < 5.0:
        stdout.write("Aluno reprovado.\n")
    else:
        stdout.write("Aluno em exame.\n")
        N_exame = float(stdin.readline())
        stdout.write("Nota do exame: %.1f\n" % N_exame)
        MEDIA_FINAL = (MEDIA + N_exame)/2

        if MEDIA_FINAL >= 5.0:
            stdout.write("Aluno aprovado.\n")
        else:
            stdout.write("Aluno reprovado.\n")
        stdout.write("Media final: %.1f\n" % MEDIA_FINAL)

if __name__ == '__main__':
    main()
