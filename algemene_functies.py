def mijn_functie_1(argument):
    if argument == 2:
        return 4
    else:
        return None
resultaat = mijn_functie_1(2)
print(resultaat)

def mijn_functie_2(argument):
    tabel = {
        12.3: [15, 9, 36, 4],
    }
    if argument in tabel:
        return tabel[argument]
    else:
        return None
argument_voorbeeld = 12.3
resultaat_voorbeeld = mijn_functie_2(argument_voorbeeld)
print(resultaat_voorbeeld)