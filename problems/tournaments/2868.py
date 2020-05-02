# 2868 - Errrou!
for _ in range(int(input())):
    exp = input().split()
    x = int(exp[0])
    y = int(exp[2])

    if exp[1] == '+':
        result = x + y
        diff = abs(int(exp[4]) - result)
        print('E{}ou!'.format(diff * 'r'))

    elif exp[1] == '-':
        result = x - y
        diff = abs(int(exp[4]) - result)
        print('E{}ou!'.format(diff * 'r'))

    elif exp[1] == 'x':
        result = x * y
        diff = abs(int(exp[4]) - result)
        print('E{}ou!'.format(diff * 'r'))

# Solution developed by Lucas Ferreira (BALSAQUE)
# for _ in range( int(input()) ):
#     exp,res = input().split(" = ")
#     n1,op,n2 = exp.split()

#     if op=="x":
#         exp = n1+"*"+n2

#     dist = abs( eval(exp)-int(res) )
#     print( "E"+dist*"r"+"ou!" )
