def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Santiago", "lastname": "Ramirez"}

    super_list = [
        {"firstname": "Santiago", "lastname": "Ramirez"},
        {"firstname": "Mateo", "lastname": "Perez"},
        {"firstname": "Pedro", "lastname": "Bonaparte"},
        {"firstname": "Arthur", "lastname": "Shelby"},
        {"firstname": "Zeus", "lastname": "Rodriguez"}
    ]

    super_dict ={
        "natural_nums": [1, 2, 3, 4, 5],
        "interger_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"], "-", item["lastname"])

if __name__ == '__main__':
    run()
