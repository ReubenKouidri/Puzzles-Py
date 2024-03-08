
def prime_finder(n):
    return [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, i))]


if __name__ == "__main__":
    print(prime_finder(11))
