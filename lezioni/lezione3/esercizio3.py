def somma(inizio, fine):
    if inizio > fine:
        temp = inizio
        inizio = fine
        fine = inizio

    risultato = 0
    for i in range(inizio, fine + 1):
        risultato += i
    return risultato

print(somma(1, 10) == 55)