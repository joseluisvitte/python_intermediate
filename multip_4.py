def run():
    # multip = [i * 4 for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and  i % 9 == 0] 

    multip = [i for i in range(1, 100000) if i % 36 == 0] 

    print(multip)
    
if __name__ == '__main__':
    run()