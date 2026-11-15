// 40.1
let rec sum (p, xs) = 
  match xs with
  | head :: tail when (p head) -> 1 + sum(p, tail)
  | head :: tail -> sum(p, tail)
  | [] -> 0

// 40.2.1
let rec count (xs: int list, n: int): int = 
  match xs with
  | head :: tail when head < n -> count (tail, n)
  | head :: tail when head = n -> 1 + count (tail, n)
  | _ -> 0 

// 40.2.2
let rec insert (xs: int list, n: int) : int list = 
  let rec _insert (xs, n, idx) = 
    match xs with
    | head :: tail when idx = 0 && n <= head -> n :: xs
    | head1 :: head2 :: tail when head1 <= n && n <= head2 -> head1 :: n :: head2 :: tail
    | head :: tail -> head :: _insert(tail, n, idx + 1)
    | [] -> [n]
  _insert (xs, n, 0)

// 40.2.3
let rec intersect (xs1: int list, xs2: int list) : int list = 
  match xs1, xs2 with
  | head1:: tail1, head2:: tail2 when head1 = head2 -> head1 :: intersect (tail1, tail2)
  | head1:: tail1, head2:: tail2 when head1 < head2 -> intersect (tail1, xs2)
  | head1:: tail1, head2:: tail2 when head1 > head2 -> intersect (xs1, tail2)
  | _, _ -> []

  

// 40.2.4
let rec plus (xs1: int list, xs2: int list): int list = 
  match xs1, xs2 with
  | head1 :: tail1, head2 :: tail2 when head1 = head2 -> head1 :: head2 :: plus(tail1, tail2)
  | head1 :: tail1, head2 :: tail2 when head1 < head2 -> head1 :: plus(tail1, xs2)
  | head1 :: tail1, head2 :: tail2 when head1 > head2 -> head2 :: plus(xs1, tail2)
  | xs1, [] -> xs1
  | [], xs2 -> xs2 
  | _, _ -> []

// 40.2.5
let rec minus (xs1: int list, xs2: int list): int list =
  match xs1, xs2 with
  | head1 :: tail1, head2 :: tail2 when head1 = head2 -> minus(tail1, tail2)
  | head1 :: tail1, head2 :: tail2 when head1 > head2 -> minus(xs1, tail2)
  | head1 :: tail1, head2 :: tail2 when head1 < head2 -> head1 :: minus(tail1, xs2)
  | xs1, [] -> xs1
  | [], xs2 -> []
  | _, _ -> []

// 40.3.1
let rec smallest (xs: int list): int option = 
  let rec _smallest (xs, n) =
    match xs with
    | head :: tail when head < n -> _smallest(tail, head)
    | head :: tail -> _smallest(tail, n)
    | [] -> n

  if xs = [] then None
  else Some(_smallest(xs, xs.[0]))

// 40.3.2
let rec delete (n: int, xs: int list): int list = 
  match xs with
  | head :: tail when n = head -> tail
  | head :: tail -> head :: delete(n, tail)
  | [] -> []

// 40.3.3
let rec sort xs = 
  let small = smallest(xs)
  match small with
  | None -> []
  | Some (value) -> value :: sort (delete(value, xs))

// 40.4
let rec revrev xs = 
  let rec rev(xs) = 
    match xs with
    | head :: tail -> (List.rev head) :: rev(tail)
    | [] -> []
  List.rev (rev xs)
