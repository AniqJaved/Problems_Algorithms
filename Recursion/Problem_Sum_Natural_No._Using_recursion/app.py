
def sum(n):
    if n==0:
        return 0
    else:
        return sum(n-1) + n


a = sum(3)
print(a)