import Data.List

dup :: (Int -> Int) -> [Int] -> [Int]
dup f [x] = [f x]
dup f (x:xs) = dup f [x] ++ dup f xs

areEven :: [Int] -> Bool
areEven xs = filter even xs == xs

squareList :: [Int] -> [Int]
squareList = map (\ x -> x * x)

sumSquares :: ([Int] -> [Int]) -> [Int] -> Int
sumSquares sq xs = foldl (+) 0 (sq (filter even xs))

isPrime :: Int -> Bool
isPrime x = _prime x (x `div` 2) where 
    _prime :: Int -> Int -> Bool
    _prime _ 1 = True
    _prime 1 _ = True
    _prime x y | mod x y == 0 = False
               | otherwise = _prime x (y - 1)

nPrimes :: Int -> [Int]
nPrimes n = take n (filter isPrime [1..])

csLists :: [Int] -> [Int] -> [Int]
csLists xs ys = sort (xs ++ ys)

main :: IO ()
main = do
    print (dup (* 2) [1, 2, 3, 4, 5]) -- [2, 4, 6, 8, 10]
    print (areEven [2, 4, 6, 8]) -- True
    print (areEven [1, 4, 6, 8]) -- False
    print(sumSquares squareList [1, 2, 3, 4]) -- 4 + 16 = 20
    print(nPrimes 10) -- 1, 2, 3, 5, 7
    print(csLists [1 ,3, 5, 7] [2, 4, 6, 8]) -- [1 2, 3, 4, 5, 6, 7, 8]