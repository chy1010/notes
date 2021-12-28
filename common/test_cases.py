def is_prime(input: int) -> bool:
    if input % 2 == 0:
        return False
    counter = 3
    while counter**2 < input:
        if input % counter == 0:
            return False
        counter += 2
    return True