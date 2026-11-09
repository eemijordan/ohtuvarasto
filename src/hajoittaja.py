def liian_pitka_rivi():
    return (
        "tämä merkkijono on tarkoituksella kirjoitettu niin pitkäksi, "
        "että rivin pituus ylittää kahdeksankymmentä merkkiä"
    )


def liikaa_sisakkaisia(luvut):
    for luku in luvut:
        if luku > 0 and luku % 2 == 0:
            print(luku)


def liikaa_parametreja(luvut):
    return sum(luvut)


def liikaa_lauseita():
    luvut = list(range(1, 17))
    return sum(luvut)
