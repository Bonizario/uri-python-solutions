# 2872 - TCP/IP Protocol
while True:
    try:
        entry = input().strip()
        if entry == "1":
            packages = []
        elif entry == "0":
            packages.sort()
            for package in packages:
                print('Package {:03d}'.format(package))
            print()
        else:
            packages.append(int(entry.split()[1]))
    except EOFError:
        break
