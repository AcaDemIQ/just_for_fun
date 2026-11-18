// 43.3
let try_find key m = 
  let lst = Map.toList m 
  let rec search lst =
    match lst with
    | [] -> None
    | head :: tail when (fst head) = key -> Some (snd head)
    | head :: tail -> search tail
  search lst
