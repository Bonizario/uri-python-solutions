def main():
    import re
    pattern = re.compile(r'^RA[0-9]{18}$')
    for _ in range(int(input())):
        ra = input().strip()
        if re.match(pattern, ra) is not None:
            password = int(ra[2:])
            print('INVALID DATA' if not password else password)
        else:
            print('INVALID DATA')
main()
