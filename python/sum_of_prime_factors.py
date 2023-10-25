import prime_finder


def is_prime(n: int) -> bool:
    if prime_finder.prime_finder(n)[0] == n:
        return True
    return False


def sum_prime_factors(n: int) -> int:
    factors = []

    if is_prime(n):
        factors.append(n)
    else:
        for i in range(2, n // 2):
            if n % i == 0:
                factors.append(i)
                factors.append(int(n / i))
                sum_prime_factors(i)
                sum_prime_factors(int(n/i))
                break

    return sum(factor for factor in factors if is_prime(factor))


if __name__ == "__main__":
    n = 75
    print(sum_prime_factors(n))
