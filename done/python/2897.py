def main():
    from sys import stdin, stdout

    while True:
        n = int(stdin.readline())
        if n == 0:
            break

        commands = list(map(int, stdin.readline().split()))
        history = {c: c for c in commands}
        ans = 0
        for command in commands:
            ans += history[command]

            for key in history:
                if key != command:
                    history[key] += 1

            history[command] = 1

        stdout.write(f'{ans}\n')

main()
