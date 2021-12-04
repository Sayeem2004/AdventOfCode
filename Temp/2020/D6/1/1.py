def main():
    f = open("1.in","r");
    f2 = open("1.out","w");
    lines = f.read().split("\n");
    ans = 0;
    s = set();
    for line in lines:
        if (line == ""):
            ans += len(s);
            s = set();
        else:
            for c in line:
                s.add(c);
    f2.write(str(ans));
main()
