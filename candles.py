def candles(a: list[int]) -> int:
    """
    Args:  a (list[int]): The candles heights.
    
    Returns: int: The number of candles that are tallest
    """
    def candles(a: list[int]) -> int:
    b = 0 # b es el quivalente de a en mi pseudo
    c = 0

    for i in range(0,len(a)-1): #no entiendo donde van los : que me marca como error en esta linea
        if candles[i] > b:
            b = candles[i]
            c = 0
            c = c + 1
        else: 
            if b == candles[i]:
                c = c + 1
     return c 


if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
