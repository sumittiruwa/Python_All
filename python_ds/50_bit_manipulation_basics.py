"""DSA Practice: Bit Manipulation Basics"""


def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def swap_without_temp(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


if __name__ == "__main__":
    print("Set bits in 29:", count_set_bits(29))
    print("Is 16 a power of two:", is_power_of_two(16))
    print("Is 18 a power of two:", is_power_of_two(18))
    print("Swap 5 and 10:", swap_without_temp(5, 10))
