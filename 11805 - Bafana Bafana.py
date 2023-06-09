t = int(input())
for i in range(1,t+1):
    n,k,p = map(int,input().split())
    count = 0
    j = 0
    while j<p:
        count = (k+j)%n
        j+=1
    print(f'Case {i}: {count+1}')

