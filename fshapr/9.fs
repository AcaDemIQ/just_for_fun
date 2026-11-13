// 23.4.1
let (.+.) (x1, x2, x3) (y1, y2, y3) =  
  let res = (x1 + y1) * 20 * 12 + (x2 + y2) * 12 + x3 + y3
  (res / 12 / 20, (res / 12) % 20, res % 12)
let (.-.) (x1, x2, x3) (y1, y2, y3) = 
  let res = x1 * 20 * 12 + x2 * 12 + x3 - (y1 * 20 * 12 + y2 * 12 + y3)
  (res / 12 / 20, (res / 12) % 20, res % 12)

// 23.4.2
let (.+) (xr: float, xi: float) (yr: float, yi: float) = (xr + yr, xi + yi)
let (.-) (xr: float, xi: float) (yr: float, yi: float) = (xr, xi) .+ (-yr, -yi)
let (.*) (xr: float, xi: float) (yr: float, yi: float) = (xr * yr - xi*yi, xi*yr + xr * yi)
let (./) (xr: float, xi: float) (yr: float, yi: float) = (xr, xi) .* (yr / (yr*yr + yi * yi), -yi / (yr*yr + yi*yi))

