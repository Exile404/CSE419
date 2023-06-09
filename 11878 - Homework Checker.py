count = 0
while True:
    try:
        s = input().split('=')

        if '+' in s[0]:
            a,b = map(int,s[0].split('+'))
        else:
            a, b = map(int, s[0].split('-'))
        try:
            c = int(s[1])
        except:
            c = ''
        if a+b == c or a-b == c:
            count+=1
    except EOFError:
        print(count)
        break
