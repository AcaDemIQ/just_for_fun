type F = 
  | AM
  | PM

type TimeOfDay = { hours: int; minutes: int; f: F }

let (.>.) (x: TimeOfDay) (y: TimeOfDay) = 
  let {hours = xh; minutes = xm; f = xf } = x
  let {hours = yh; minutes = ym; f = yf } = y
  if xf = AM && yf = PM then false
  elif xf = PM && yf = AM then true
  else (xh, xm) > (yh, ym)

