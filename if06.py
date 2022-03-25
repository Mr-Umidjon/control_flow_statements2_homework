def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n = str(n)

    max_index = 0
    maximum = n[0]
    if maximum < n[1]:
        max_index = 1
    if maximum < n[2]:
        max_index = 2
    if maximum < n[3]:
        max_index = 3
    if maximum < n[4]:
        max_index = 4
    return max_index+1


print(main(16325))
