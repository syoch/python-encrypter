import re
import sys
table = {
    0: "b",
    1: "c",
    2: "d"
}


def conv(a: int):
    if a in table:
        return table[a]
    if a <= 2:
        raise "a"
    elif a % 2 == 0:
        b = "d*"
        b += conv(a//2)
        b = b
        table[a] = b
        return b
    else:
        b = "d*"
        b += conv((a-1)//2)
        b += "+c"
        b = "("+b+")"
        table[a] = b
        return b


def convstr(a, f="f"):
    d = []
    for b in a:
        d.append(f+"("+conv(ord(b))+")")
    return "+".join(d)


def convexec(a, f="f"):
    return f"e({convstr(a,f=f)})"


def filter_space(array):
    return filter(lambda x: x != "", array)


s = ""
s += "a=eval\n"
s += "b=len([])\n"
s += "c=range(len([])**len([])+len([])**len([]))[len([])**len([])]\n"
s += "d=+True+True\n"
s += "f=a(\"chr\")\n"
s += "e=a(\"exec\")\n"
s += "g=\"\"\n"
src = open(sys.argv[1]).read()
for line in filter_space(re.split("([\x00-\uffff])", src)):
    s += "g+="+convstr(line)+"\n"
s += "e(g)"
open(sys.argv[2], "w").write(s)
