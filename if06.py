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

    max_index = 1
    maximum = x1
    if maximum < x2:
        max_index = 2
    if maximum < x3:
        max_index = 3
    if maximum < x4:
        max_index = 4
    if maximum < x5:
        max_index = 5
    return max_index


print(main(16325))
