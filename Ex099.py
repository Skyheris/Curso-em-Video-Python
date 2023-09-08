from time import sleep

print("-="*15)


def maior(*núm):
    mai = cont = 0
    print("Analisando os valores registados...")
    for n in núm:
        print(f"{n}", end=" ")
        sleep(0.4)
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1

    print(f"Foram registados {len(núm)} valores ao todo.")
    print(f"O maior valor registado foi {mai}")
    print("-="*15)


maior(2, 5, 7, 8, 1, 6)
maior(5, 8, 9)
maior(7, 1)
maior(5)
maior()