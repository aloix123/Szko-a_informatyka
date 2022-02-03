def nwd(a,b):
    while b!=0:

        c=a%b
        a=b
        b=c
    return a
def nww(a,b):
    return(a*b)//nwd(a,b)
print(nww(12,128))
