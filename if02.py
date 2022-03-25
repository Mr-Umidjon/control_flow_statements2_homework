def main(a, b, c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    minimum = a
    if minimum > b:
        minimum = b

    if minimum > c:
        minimum = c

    return minimum
