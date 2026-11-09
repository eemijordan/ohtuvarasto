def liian_pitka_rivi():
    return "tämä merkkijono on tarkoituksella kirjoitettu niin pitkäksi, että rivin pituus ylittää kahdeksankymmentä merkkiä"


def liikaa_sisakkaisia(luvut):
    for luku in luvut:
        if luku > 0:
            if luku % 2 == 0:
                print(luku)


def liikaa_parametreja(a, b, c, d):
    return a + b + c + d


def liikaa_lauseita():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p
