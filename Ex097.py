def texto(txt):
    tamanho =int((len(txt) / 2) + 2 )
    print("-=" * tamanho)
    print(f"  {txt:^}")
    print("-=" * tamanho)


texto("Olá Mundo!")
texto("Bom dia Alegria!")
texto("Olá!")



