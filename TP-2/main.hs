mapSucesor :: [Int] -> [Int]
mapSucesor [] = []
mapSucesor (x:xs) = [x + 1] ++ mapSucesor xs

filterPositive :: [Int] -> [Int]
filterPositive [x] = if x > 0 then [x] else []
filterPositive (x:xs) = filterPositive [x] ++ filterPositive xs

l :: [a] -> Int
l [] = 0
l (x:xs) = 1 + l xs

mapLong :: [[a]] -> [Int]
mapLong [] = []
mapLong (x:xs) = [l x] ++ mapLong xs

main = do
    print(mapSucesor [1, 2, 3, 4, 5])
    print(filterPositive [1, 2, -1, 0, 7, -8])
    print(mapLong [[1, 2], [], [1, 1, 1], [1, 7, 8, 4, 8]])