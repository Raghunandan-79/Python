def demo():
    print("Hello world")

def sum_of_two_numbers(a, b):
    print(a + b)

def difference_of_two_numbers(a, b):
    return a - b

def divide(a, b = 2):
    return a // b

def main():
    demo()
    sum_of_two_numbers(3, 4)
    result = difference_of_two_numbers(3, 5)
    print(result)
    print(divide(5))
    print(difference_of_two_numbers(a=6, b=2))

if __name__ == "__main__":
    main()