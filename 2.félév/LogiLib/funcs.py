def factorial(n: int) -> int:
    """
    Kiszámolja egy szám faktoriálisának az értékét.\n
    Paraméterek:\n
        n (int): A szám aminek a faktoriálisát akarjuk nézni\n
    Visszatérési érték:\n
        int típus, az n faktoriális értéke\n
    Hibák:\n
        ValueError: negatív int esetén
        TypeError:  nem int n paraméter esetén
    """ # Ez a függvény docstringje
    if type(n) != int:
        raise TypeError("A factorial függvénynek csak nem negatív egész számot lehet megadni!")
    if n < 0:
        raise ValueError("Negatív faktoriálist nem lehet megadni!")
    if n < 2:
        return 1
    return n * factorial(n-1)

def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    This function computes the nth number in the Fibonacci sequence using 
    memoization for efficient recursive calculation.

    Args:
        n (int): The position in the Fibonacci sequence to calculate.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        >>> fib(1)
        1
        >>> fib(5)
        5
        >>> fib(10)
        55
    """
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    def f(n, memo = {}):
        if n in memo.keys():
            return memo[n]
        if n == 1 or n == 2:
            return 1
        memo[n] = f(n-1, memo) + f(n-2,memo)
        return memo[n]
    return f(n)
    