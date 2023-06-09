t =int(input())
for i in range(1,t+1):
    a,b,c = map(int,input().split())
    sum = a+b+c
    ans = sum-max(a,b,c)-min(a,b,c)
    print(f'Case {i}: {ans}')