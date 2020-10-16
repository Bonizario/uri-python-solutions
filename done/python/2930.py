def main():
    from sys import stdin, stdout

    delivered, deadline = map(int, stdin.readline().split())
    delta = deadline - delivered
    if delta < 0:
        stdout.write('Eu odeio a professora!\n')
    elif delta >= 3:
        stdout.write('Muito bem! Apresenta antes do Natal!\n')
    else:
        stdout.write('Parece o trabalho do meu filho!\n')
        delivered += 2
        stdout.write('TCC Apresentado!\n' if delivered < 24 else 'Fail! Entao eh nataaaaal!\n')

main()
