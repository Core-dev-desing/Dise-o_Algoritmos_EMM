def Fibonachi(n):
    dict{
        0:1
        1:1
    }
    if n<=1:
        return 1
    else:
        Fibonachi(n)=Fibonachi(n-1)+Fibonachi(n-2)
    return Fibonachi(n)
