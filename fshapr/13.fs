// 39.1
let rec rmodd = function
  | [] -> []
  | [x] -> []
  | head1 :: head2 :: tail -> head2 :: (rmodd tail)

// 39.2
let rec del_even list = 
  match list with
  | head :: tail when head % 2 = 0 -> del_even tail
  | [] -> []
  | head :: tail -> head :: del_even tail

// 39.3
let rec multiplicity x xs = 
  match xs with
  | head :: tail when head = x -> 1 + (multiplicity x tail)
  | head :: tail -> multiplicity x tail
  | [] -> 0

// 39.4
let rec split l = 
  let rec fmodd = function
    | [] -> []
    | [x] -> [x]
    | head1 :: head2 :: tail -> head1 :: (fmodd tail)
  (fmodd l, rmodd l)

// 39.5
let rec zip (xs1, xs2) = 
  match (xs1,xs2) with
  | (xs1,xs2) when List.length xs1 <> List.length xs2 -> failwith "non eq lengths"
  | (head1 :: tail1, head2::tail2) -> (head1, head2) :: zip (tail1, tail2)
  | ([], []) -> []
