#!/usr/bin/python3

"""
fewest number of coins needed to meet total    
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
        Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
"""
    sortArr = sorted(coins)
    reversedCoin = sortArr[::-1]
    ans = 0
    for i in reversedCoin:
        if total > i:
            result = int(total / i)
            total = total % i
            ans = ans + result
    if total == 0:
        return(ans)
    else:
        return(-1)
