from math import sqrt
def run():
    # numbers = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         numbers[i] = i**3

    # numbers = {i: i**3 for i in range(1,101) if i % 3 != 0}

    numbers = {i: round(sqrt(i),2) for i in range(1, 101)}
    print(numbers)



if __name__ == '__main__':
    run()