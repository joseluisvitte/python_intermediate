def run():
    my_list = [1, "Hello", True, 4.5]
    my_dic = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Luis", "lastname": "Escamilla"},
        {"firstname": "Abraham", "lastname": "Lopez"},
        {"firstname": "Rogelio", "lastname": "Escamilla"},
        {"firstname": "Cecilia", "lastname": "Vite"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "foating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()