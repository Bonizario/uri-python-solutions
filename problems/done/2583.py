# 2583 - Chirrin Chirrion
for _ in range(int(input())):
    requests = set()

    for _ in range(int(input())):
        item, request = input().split()
        if request == 'chirrin':
            requests.add(item)
        elif request == 'chirrion' and item in requests:
            requests.remove(item)

    print('TOTAL')
    for request in sorted(requests):
        print(request)
