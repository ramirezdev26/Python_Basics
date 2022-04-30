import random
import os
def read():
    os.system("clear")
    print("Adivina la palabra!")
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
    random_word = random.choice(words)

    enumerated_word = list(enumerate(random_word.replace("\n", "")))
    #print(enumerated_word)
    unde_list = ["_"] * len(enumerated_word)
    string = ""
    for a in unde_list:
        string += " " + a
    print(string)
    unde_list = list(enumerate(unde_list))
    
    
    while enumerated_word != unde_list:
        
        keys = []
        string = ""
        letter = input("Ingresa una letra: ")
        for d, value in enumerated_word:
            if letter == value:
                keys.append(d)
        for i, v in unde_list:
            for j in keys:
                if j == i:
                    unde_list[i] = (i, letter)
        os.system("clear")
        print("Adivina la palabra!")
        for b, c in unde_list:
            string += " " + c
        print(string)
            
        

            # stri_a = ""
            # for i in unde_list:
            #     stri_a += " " + i
            # print(stri_a)


def run():
    read()
    
    



if __name__ == '__main__':
    run()

    