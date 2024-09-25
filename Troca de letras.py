while True:
    palavra = [x for x in input().upper()]
    for i in range(len(palavra)):
        if palavra[i] == "3":
            del palavra[i]
            palavra.insert(i, "E")
        if palavra[i] == "4":
            del palavra[i]
            palavra.insert(i, "A")
        if palavra[i] == "1":
            del palavra[i]
            palavra.insert(i, "I")
        if palavra[i] == "5":
            del palavra[i]
            palavra.insert(i, "S")
    minhapalavra = "".join(palavra)
    if minhapalavra == "SAIR" or minhapalavra == "FIM":
        break
    else:
        print(minhapalavra)
