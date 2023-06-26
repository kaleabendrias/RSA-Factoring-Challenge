#!/usr/bin/python3
import sys


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n // = i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return (factors)


def main():
    if (len(sys.argv) != 2):
        print("Usage: factors <file>")
        return
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                n = int(line.strip())
                factors = factorize(n)
                result = f"{n}={factors[0]}*{factors[1]}"
                print(result)
    except FileNotFoundError:
        print("File '{}' not found.".format(file_path))
    except ValueError:
        print("Invalid numbers in the file.")


if __name__ == "__main__":
    main()
