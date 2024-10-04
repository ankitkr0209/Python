


def mul_all(*args):
    print(args)

    result = 1

    for i in args:
        result = result*i
    
    return result


print(mul_all(1,2,3,4))

print(mul_all(3,4,5,2,7,8,9))

print(mul_all(23,43,232,22,1))





