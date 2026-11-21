// 49.5.1
let even_seq = Seq.initInfinite (fun i -> 2*(i+1))


// 49.5.2
let rec fac_rec i c = 
  match i with
  | 0 -> c 1
  | n -> fac_rec (n - 1) (fun f -> c (n * f))

let fac_seq = Seq.initInfinite (fun i -> fac_rec i id)

// 49.5.3
let num_s n =
  match n with
  | 0 -> 0
  | n when n % 2 <> 0 -> -1 * (n + 1)/2
  | n -> n / 2

let seq_seq = Seq.initInfinite(num_s)
