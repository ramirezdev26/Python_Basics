import py_compile

def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0: 
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # print(squares)

    numbers = [i for i in range(1, 999999) if i % 36 == 0]

    print(numbers)

if __name__ == '__main__':
    run()