def main():
    f = open("2.in","r");
    f2 = open("2.out","w");
    lines = f.read().split("\n");
    ans = 0; i = 0;
    s = set();
    for line in lines:
        if (line == ""):
            ans += len(s);
            s = set();
            i = 0;
        else:
            if (i == 0):
                for c in line:
                    s.add(c);
                i = 1;
            else:
                l = [];
                for c in s:
                    if (not c in line):
                        l.append(c);
                for c in l:
                    s.discard(c);
    f2.write(str(ans));
main()
