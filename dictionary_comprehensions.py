def run():
    #nature_num = {}

    #for i in range(1, 101):
    #    if i % 3 != 0:
    #        nature_num[i] = i ** 3

    nature_num = {i: i**3 for i in range(1, 101) if i %3 != 0}

    print(nature_num)

if __name__ == '__main__':
    run()