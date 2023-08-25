from functools import reduce

nums = [num for num in range(1,11)]

def main():
    try:
        product = reduce(lambda x,y: x*y, nums)
        return product
    except TypeError as err:
        print(f"{err}: needs values added to the list.")

if __name__ == "__main__":
    print(main())

