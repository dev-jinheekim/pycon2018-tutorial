# pycon2018 간단한 언어 만들기 실습 한자리 수 계산기
# 1단계: 1+2-3
# 2단계: 1+2*3-8/4
# 3단계: 1+2*(3-4)


def num(par):
    v = int(par[0])
    s = par[1:]
    return v, s


def expr(par):
    v, s = num(par)
    while s:
        if s[0] == '+':
            v += int(s[1])
        elif s[0] == '-':
            v -= int(s[1])
        else:
            break
        s = s[2:]
    return v, s


def parse():
    v, _ = expr(input())
    return v


print(parse())
