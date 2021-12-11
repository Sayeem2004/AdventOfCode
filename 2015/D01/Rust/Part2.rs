use std::fs;

fn main() {
    let fin = fs::read_to_string("../input.in").expect("Input Error");
    fs::write("../part2.out",solve(fin)).expect("Output Error");
}

fn solve(fin: String) -> String {
    let mut floor: i32 = 0;
    for (i,c) in fin.chars().enumerate() {
        if c == '(' {floor += 1;}
        if c == ')' {floor -= 1;}
        if floor == -1 {return (i+1).to_string()}
    }
    return 0.to_string();
}
