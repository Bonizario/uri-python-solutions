def main():
    import re

    day = {
        '1': 'MONDAY',
        '2': 'MONDAY',
        '3': 'TUESDAY',
        '4': 'TUESDAY',
        '5': 'WEDNESDAY',
        '6': 'WEDNESDAY',
        '7': 'THURSDAY',
        '8': 'THURSDAY',
        '9': 'FRIDAY',
        '0': 'FRIDAY',
    }
    pattern = re.compile(r'^[A-Z]{3}-[0-9]{4}$')
    for _ in range(int(input())):
        s = input().strip()
        if re.match(pattern, s) is not None:
            print(day[s[-1]])
        else:
            print('FAILURE')
main()
