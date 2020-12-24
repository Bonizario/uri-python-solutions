def main():
    d = {
        'W': 1,
        'H': 0.5,
        'Q': 0.25,
        'E': 0.125,
        'S': 0.0625,
        'T': 0.03125,
        'X': 0.015625
    }

    while True:
        s = input().strip()
        if s == '*':
            break
        s = s.strip('/').split('/')
        total = 0
        for compasso in s:
            aux = 0
            for note in compasso:
                aux += d[note]
            if 0.99999 <= aux <= 1.000001:
                total += 1
        print(total)

main()
