def main():
    from sys import stdin, stdout
    regras = {
        'te': {'pa', 'la'},
        'pa': {'pe', 'sp'},
        'pe': {'la', 'te'},
        'la': {'sp', 'pa'},
        'sp': {'te', 'pe'}
    }
    for _ in range(int(stdin.readline())):
        entry = stdin.readline().strip().split()
        raj, sheldon = entry[0][:2], entry[1][:2]
        if raj == sheldon:
            stdout.write('empate\n')
        elif raj in regras[sheldon]:
            stdout.write('sheldon\n')
        else:
            stdout.write('rajesh\n')
main()
