use std::fs;

fn main() {
    let fin = fs::read_to_string("../Input.in").expect("Input Error");
    fs::write("../Part1.out",solve(fin)).expect("Output Error");
}

fn solve(fin: String) -> String {
    let mut floor: i32 = 0;
    for c in fin.chars() {
        if (c == '(') {floor += 1;}
        if (c == ')') {floor -= 1;}
    }
    return floor.to_string();
}
