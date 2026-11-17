// 41.4.1
let list_filter f xs = List.foldBack (fun head tail -> if (f head) then head :: tail else tail) xs []

// 41.4.2
let sum (p, xs) = List.foldBack (fun head tail -> if (p head) then head + tail else tail) xs 0

// 41.4.3
let revrev lst = 
  let rev lst = List.fold (fun head tail -> tail::head) [] lst
  List.fold (fun head tail -> (rev tail)::head) [] lst
