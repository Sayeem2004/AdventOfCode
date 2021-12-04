use std::fs;

fn main() {
    let fin = fs::read_to_string("../Input.in").expect("Input Error");
    fs::write("../Part1.out",solve(fin)).expect("Output Error");
}

fn solve(fin: String) -> String {
    let mut count: i32 = 0;
    let numbers: Vec<&str> = fin.split('\n').collect();
    for number in &numbers[0..numbers.len()-1] {
        let num: Vec<&str> = number.split('x').collect();
        let mut nums: Vec<i32> = vec![];
        for n in &num {nums.push(n.parse().unwrap_or(0));}
        nums.sort();
        count += 3*nums[0]*nums[1];
        count += 2*nums[0]*nums[2];
        count += 2*nums[1]*nums[2];
    }
    return count.to_string();
}
