text = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

lines = text.split("\n")
lines = [s.strip() for s in open("p25.txt").readlines()]

def snafu_to_dec(s):
    tot = 0
    for i in range(0, len(s)):
        ch = s[-1-i]
        base = 5 ** i
        if ch in "012": num = int(ch)
        elif ch == "-": num = -1
        elif ch == "=": num = -2
        tot += num * base
    return tot

def dec_to_snafu(x):
    snafu = ""
    while x:
        n = x % 5
        if n <= 2:
            s = str(n)
            x -= n
        elif n == 3: 
            s = "="
            x += 2
        elif n == 4:
            s = "-"
            x += 1
        x = x // 5
        snafu = snafu + s
    return snafu[::-1]

tot = sum(snafu_to_dec(s) for s in lines)
print(tot)
print(dec_to_snafu(tot))


