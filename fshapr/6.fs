// 17.1
let rec pow = function
  | (s, n) when n = 0 -> ""
  | (s, n) -> s + pow(s, n-1)

// 17.2
let rec isIthChar = function
  | (s, n ,c) when (String.length s) <= n || n < 0  -> false
  | (s, n, c) -> s.[n] = c

// 17.3
let rec occFromIth = function
  | (s, n, c) when (String.length s) = n -> 0
  | (s, n, c) when isIthChar(s, n, c) -> 1 + occFromIth(s, n+1, c)
  | (s, n, c) -> occFromIth(s, n+1, c) 
