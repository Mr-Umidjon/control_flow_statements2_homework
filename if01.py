def main(a, b, c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    maximum = a
    if maximum < b:
        maximum = b
    if maximum < c:
        maximum = c
    return maximum
