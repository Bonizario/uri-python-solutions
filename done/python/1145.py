# 1145 - Logical Sequence 2
def main():
    from sys import stdin, stdout
    X, Y = [int(x) for x in stdin.readline().split()]
    counter = 0
    nums_list = ''
    for i in range(1, Y + 1):
        nums_list += str(i)
        counter += 1
        if counter == X:
            nums_list += '\n'
            counter = 0
        else:
            nums_list += ' '
    stdout.write(nums_list)

if __name__ == '__main__':
    main()

"""
X, Y = map(int, input().split())
counter = 0
nums_list = ""
for i in range(1, Y + 1):
    nums_list += str(i)
    counter += 1
    if counter == X:
        nums_list += "\n"
        counter = 0
    else:
        nums_list += " "
final_list = nums_list.strip("\n")
print(final_list)
"""
