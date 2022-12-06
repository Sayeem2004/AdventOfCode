use std::fs;

fn main() {
    let fin = fs::read_to_string("input.in").expect("Input Error");

    println!("Part 1: {}", part1(&fin));
    println!("Part 2: {}", part2(&fin));
}

fn part1(fin: &String) -> String {
    let mut floor: i32 = 0;

    for c in fin.chars() {
        if c == '(' {
            floor += 1;
        }
        if c == ')' {
            floor -= 1;
        }
    }

    floor.to_string();
}

fn part2(fin: &String) -> String {
    let mut floor: i32 = 0;

    for (i, c) in fin.chars().enumerate() {
        if c == '(' {
            floor += 1;
        }
        if c == ')' {
            floor -= 1;
        }
        if floor == -1 {
            return (i + 1).to_string();
        }
    }

    0.to_string();
}
