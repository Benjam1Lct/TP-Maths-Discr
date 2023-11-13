def division(a, b):
    quotient = 0
    while a >= b:
        quotient += 1
        a = a-b
    return quotient, a

def euclide(a ,b):
    u0, u1, v0, v1 = 1,0,0,1
    r = 0
    q, r = division(a, b)
    while r != 0:
        a = b
        b = r   
        u0, u1 = u1, u0-q*u1
        v0, v1 = v1, v0-q*v1
        q, r = division(a, b)
    return b, (u1, v1)
             

if __name__ == '__main__':
    a = 14
    b = 3
    print(euclide(a, b))