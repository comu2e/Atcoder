use proconio::input;
const MOD:u64 = 100000007;
fn main() {
  input! {
      n: usize,
      a: [u64; n],
  }
  let mut a: Vec<(usize, u64)> = a.iter().copied().enumerate().collect();
  a.sort_by_key(|b| b.1);
  println!("{}", a[a.len() - 2].0 + 1);
}
