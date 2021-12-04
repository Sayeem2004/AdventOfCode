def main():
    f = open("2.in","r");
    f2 = open("2.out","w");
    lines = f.read().split("\n");
    lines = [line.split(" ") for line in lines];
    count = 0;
    c = 0;
    a = False;
    h = ["amb","blu","brn","gry","grn","hzl","oth"];
    for pp in lines:
        for id in pp:
            if (id[0:3] == "byr" and int(id[4:]) >= 1920 and int(id[4:]) <= 2002):
                c+=1;
                continue;
            if (id[0:3] == "iyr" and int(id[4:]) >= 2010 and int(id[4:]) <= 2020):
                c+=1;
                continue;
            if (id[0:3] == "eyr" and int(id[4:]) >= 2020 and int(id[4:]) <= 2030):
                c+=1;
                continue;
            if (id[0:3] == "hgt"):
                if (id[len(id)-2:] == "cm"):
                    x = int(id[4:len(id)-2]);
                    if (x >= 150 and x <= 193):
                        c+=1
                elif (id[len(id)-2:] == "in"):
                    x = int(id[4:len(id)-2]);
                    if (x >= 59 and x <= 76):
                        c+=1;
                continue;
            if (id[0:3] == "hcl" and len(id)-4 == 7 and id[4] == "#"):
                c+=1;
                continue;
            if (id[0:3] == "ecl" and id[4:] in h):
                c+=1;
                continue;
            if (id[0:3] == "pid" and len(id[4:]) == 9):
                c+=1;
                continue;
            if (id[0:3] == "cid"):
                a = True;
                c+=1;
                continue;
            if (len(id) == 0):
                c = 0;
                a = False;
                continue;
        if (c == 8 or (c == 7 and not a)):
            count+=1;
            c = 0;
            a = False;
    f2.write(str(count));
    f2.write("\n");
main()
