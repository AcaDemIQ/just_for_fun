// 50.2.1
let fac_seq = seq {
  yield 1
  let mutable acc1: int = 1
  for i in Seq.initInfinite (fun i -> i + 1) do
    acc1 <- acc1 * i
    yield acc1  }

// 50.2.2
let seq_seq = seq {
  for i in Seq.initInfinite (fun i -> i) do
    if i = 0 then
      yield i
    elif i % 2 = 0 then
      yield (i / 2)
    else yield ((-1)* (i + 1) / 2)  }

