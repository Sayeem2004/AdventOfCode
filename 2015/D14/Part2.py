fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" ") for line in lines];
    lines = [[int(line[3]),int(line[6]),int(line[-2])] for line in lines];
    dist = {}; points = {};
    for i in range(len(lines)):
        dist[i] = 0;
        points[i] = 0;
    fout.write(str(solve(lines,2503,dist,points)));

def solve(lines,time,dist,points):
    for i in range(time):
        for q,line in enumerate(lines):
            if (i%(line[1]+line[2]) < line[1]):
                dist[q] += line[0];
        mx = 0;
        for d in dist:
            mx = max(dist[d],mx);
        for d in dist:
            if (dist[d] == mx):
                points[d] += 1;
    ans = 0;
    for p in points:
        ans = max(points[p],ans);
    return ans;

main();
