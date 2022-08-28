def multiply(a, b):
    """
    Multiply by adding a and b together and returning the result
    multiply(2,1) ->2    2 + 0    | 1 + 1 + 0
    
    multiply(3,2) ->6    3 + 3 + 0 | 2 + 2 + 2 + 0
    
    What stops it?
    Return a call to itself
    Keep track of the number of calls -> Counter --
    """
    if b == 0:
        return b
    else:
        return a + multiply(a, b - 1)


if __name__ == '__main__':
    print(multiply(2, 1))
    print(multiply(3, 2))
