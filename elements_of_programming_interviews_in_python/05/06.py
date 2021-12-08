def max_profit_from_list(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0.0

    for price in prices:
        profit_sell = price - min_price
        max_profit = max(max_profit, profit_sell)
        min_price = min(min_price, price)

    return max_profit


if __name__ == "__main__":
    assert max_profit_from_list([310, 315, 275, 295, 260, 270, 290,230, 255, 250]) == 30

