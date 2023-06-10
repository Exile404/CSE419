dovrak = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?";
qwerty =  "`123qjlmfp/[]456.orsuyb;=\\789aehtdck-0zx,inwvg'~!@#QJLMFP?{}$%^>ORSUYB:+|&*(AEHTDCK_)ZX<INWVG\"";

# print(len(dovrak))
# print(len(qwerty))
dic= {}
for i in range(len(dovrak)):
    dic[dovrak[i]] = qwerty[i]
# print(dic)

while True:
    try:
        s= input()
        s1 = ''
        for i in range(len(s)):
            if s[i]==' ':
                s1+=' '
            else:
                s1+=dic[s[i]]
        print(s1)
    except EOFError:
        break
