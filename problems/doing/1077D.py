# 1077 - Infix to Posfix
# for _ in range(int(input())):
#     exp = input()
#     posfix = ''
#     parenthesis = []
#     operations = []
#     inside = False
#     for i in range(len(exp)):
#         if exp[i] == '(':
#             parenthesis.append(tuple(('(', i)))
#         elif exp[i] == ')':
#             parenthesis.append(tuple((')', i)))
#         elif exp[i] == '^':
#             operations.append(tuple((0, i)))
#         elif exp[i] == '*':
#             operations.append(tuple((1, i)))
#         elif exp[i] == '/':
#             operations.append(tuple((1, i)))
#         elif exp[i] == '+':
#             operations.append(tuple((2, i)))
#         elif exp[i] == '-':
#             operations.append(tuple((2, i)))
#     for i in range(len(exp)):
