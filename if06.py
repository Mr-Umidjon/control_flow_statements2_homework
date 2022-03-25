def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n % 10
    n //= 10

    x2 = n % 10
    n //= 10

    x3 = n % 10
    n //= 10

    x4 = n % 10
    n //= 10

    x5 = n % 10
    n //= 10

    maximum = x1
    index = 1
    if maximum < x2:
        maximum = x2
        index = 2
    if maximum < x3:
        maximum = x3
        index = 3
    if maximum < x4:
        maximum = x4
        index = 4
    if maximum < x5:
        maximum = x5
        index = 5
    return index


print(main(16325))
