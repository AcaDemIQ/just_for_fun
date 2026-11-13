// 34.1
let rec upto n = 
  let rec _upto = function
    | (n, m) when m > n -> []
    | (n, m) -> m :: _upto (n, m+1)
  _upto (n, 1)

// 34.2
let rec dnto (n: int) = 
  let rec _dnto = function
    | (current, acc) when current > n -> acc
    | (current, acc) -> _dnto (current + 1, current :: acc)
  _dnto (1, [])

// 34.3
let rec evenn n = 
  let rec _even = function
    | (current, acc) when current < 0 -> acc
    | (current, acc) -> _even (current - 2, current :: acc)
  _even (2*(n-1), [])
