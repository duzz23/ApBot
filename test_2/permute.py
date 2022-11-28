import argparse
from sympy.utilities.iterables import multiset_permutations
import time


def main():
    number = int(5)
    start_time = time.time()
    parser = argparse.ArgumentParser(description='Program for seeking digits and proper nouns')
    parser.add_argument('amount', nargs='?', help='Amount of numbers', default=number, type=int)
    args = parser.parse_args()

    numbers = [0]*args.amount + [i for i in range(1, args.amount+1)]

    for result in multiset_permutations(numbers):
        print(result)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()