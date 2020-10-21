def main():
    import re
    pattern = re.compile(r'.{1}oulupukk.{1}')
    for _ in range(int(input())):
        text = input()
        print(re.sub(pattern, 'Joulupukki', text))
main()
