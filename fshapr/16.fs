let rec allSubsets n k = 
  let genList = [1..n]
  
  let rec allSubsetsLst lst =
    match lst with
    | [] -> [[]]
    | x :: xs -> let subset = allSubsetsLst xs
                 subset @ List.map (fun s -> x :: s) subset
  
  allSubsetsLst genList |> List.map Set.ofList |> List.filter (fun s -> Set.count s = k) |> Set.ofList

  
