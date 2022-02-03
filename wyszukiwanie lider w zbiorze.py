n=int(input())
T=list(map(int,input().split()))
print(T)
T.sort()
print(T)
if T.count(T[n//2])>n//2:
    print(T[N//2])
else:
    print('nie ma')