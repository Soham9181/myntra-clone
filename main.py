s = int(input())
def ntozero(n):
    print(n, ntozero(n-1) if n>0 else '')
ntozero(s)