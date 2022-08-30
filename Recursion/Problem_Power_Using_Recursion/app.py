def fun(m,n):
    if n==0:
        return 1
    else:
        return fun(m,n-1) * m

a = fun(2,5)
print(a)