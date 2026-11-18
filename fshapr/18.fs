// 47.4.1
let f n = 
  let mutable i = n
  let mutable r = 1
  while i > 0 do
    r <- r * i
    i <- i - 1
  r

// 47.4.2
let fibo n = 
  let mutable i = 0
  if n = 0 then
    0
  elif n = 1 then
    1
  else
    i <- 2
    let mutable f = 0
    let mutable s = 1
    let mutable t = 0
    while i <= n do
      t <- f + s
      f <- s
      s <- t
      i <- i + 1
    t
