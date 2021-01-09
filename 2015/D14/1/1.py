fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" ") for line in lines];
    lines = [[int(line[3]),int(line[6]),int(line[-2])] for line in lines];
    dist = {};
    for i in range(len(lines)):
        dist[i] = 0;
    fout.write(str(solve(lines,2503,dist)));

def solve(lines,time,dist):
    for i in range(time):
        for q,line in enumerate(lines):
            if (i%(line[1]+line[2]) < line[1]):
                dist[q] += line[0];
    ans = 0;
    for d in dist:
        ans = max(dist[d],ans);
    return ans;

main();
