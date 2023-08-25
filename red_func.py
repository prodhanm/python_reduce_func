from functools import reduce

nums = [num for num in range(1,11)]

def main():
    product = reduce(lambda x,y: x*y, nums)
    return product

if __name__ == "__main__":
    print(main())

