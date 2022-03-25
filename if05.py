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
    elif maximum < x3:
        maximum = x3
    elif maximum < x4:
        maximum = x4
    else:
        maximum = x5
    return maximum
