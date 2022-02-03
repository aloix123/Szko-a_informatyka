
# a -słupek żrudłowy
#b-słupek docelowy
#n-liczba krążkó
#p-pomocniczy słupek


def hanoi(a,b,n,d):
    if n==1:
        d += 1
        print(f'{d} przenieś krążek {n} z {a} na {b}')
        return d
    else:
        p=6-a-b
        d=hanoi(a,p,n-1,d)
        d+=1
        print(f'{d} przenieś krążek {n} z {a} na {b}')

        d=hanoi(p,b,n-1,d)
        return d
hanoi(1,2,5,0)




































