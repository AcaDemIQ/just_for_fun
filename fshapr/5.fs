// 16.1
let notDivisible = function
    | (n, m) when m % n = 0 -> true
    | _ -> false


// 16.2
let  prime n =
  let rec _prime = function
    | (n, m) when n = m -> true
    | (n, m) when notDivisible(m, n) -> false
    | (n, m) -> _prime(n, m+1)
  _prime(n, 2)
