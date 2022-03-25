def main(n):
    """
    Find the largest digit of the five-digit number.
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
    if maximum < x2:
        maximum = x2
    if maximum < x3:
        maximum = x3
    if maximum < x4:
        maximum = x4
    if maximum < x5:
        maximum = x5
    return maximum
