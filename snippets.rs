use std::fs;

fn main() {
    let fin = fs::read_to_string("../Input.in").expect("Input Error");
    fs::write("../Part.out",solve(fin)).expect("Output Error");
}

fn solve(lines : String) -> String {

}
