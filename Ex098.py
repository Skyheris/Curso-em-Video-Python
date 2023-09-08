from time import sleep


def contador():
    print("-=" * 10)
    print("Contagem de 1 até 10 de 1 em 1")
    for c in range(1, 11):
        print(c, end=" ")
        sleep(0.3)
    print("FIM!", end="")
    print()
    print("-=" * 10)
    print("Contagem de 10 até 0 de 2 em 2")
    sleep(0.5)
    for num in range(10, -1, -2):
        print(num, end=" ")
        sleep(0.3)
    print("FIM!")
    print("-="*10)

    i = int(input("Início: "))
    f = int(input("Fim: "))
    p = int(input("Passo: "))

    if i < f:
        for num in range(i, f + 1, p):
            print(num, end=" ")
            sleep(0.3)
        print("FIM!")
    else:
        for num in range(i, f - 1, -p):
            print(num, end=" ")
            sleep(0.3)
        print("FIM!")


contador()
