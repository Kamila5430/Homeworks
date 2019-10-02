def plus(x, y):
    s = []
    if len(x)>len(y):
        y.insert(0,0)
    elif len(x)<len(y):
        x.insert(0,0)
    for i in range(len(x)):
        s.append(x[i] + y[i])
    for k in s:
        for i in range(len(s)):
            if s[i]>=10:
                s[i-1]+=1;
                s[i]-=10;
    return s
def minus(x, y):
    s = []
    if len(x)>len(y):
        y.insert(0,0)
    elif len(x)<len(y):
        x.insert(0,0)
    r = int("".join(map(str, x)))
    r1 = int("".join(map(str, y)))
    if r<r1:
        for i in range(len(y)):
            s.append(y[i] - x[i])
        for k in s:
            for i in range(len(s)):
                if s[i] < 0:
                    s[i - 1] -= 1;
                    s[i] += 10;
        s.insert(0,'-')
    else:
        for i in range(len(x)):
            s.append(x[i] - y[i])
        for k in s:
            for i in range(len(s)):
                if s[i] < 0:
                    s[i - 1] -= 1;
                    s[i] += 10;
    return s

x1 = [1, 2, 4, 4]
y1 = [4, 5, 6]
print(plus(x1, y1))
print(minus(x1, y1))
print(minus(y1, x1))