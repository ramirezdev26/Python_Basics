def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding = "utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)


def write():
    animals = ["Perro", "Gato", "Tortuga", "Pajaro"]
    with open("./archivos/animals.txt", "a", encoding="utf-8") as f:
        for animal in animals:
            f.write(animal)
            f.write("\n")



def run():
    write()

if __name__ == '__main__':
    run()