daudzums = int(input("cik skaitļu ievadīsi?"))

if daudzums <= 0:
    print("Kļuda skaitļu skaitam jābūt lielākam par 0.")
else:
    skaitlis = int(input("Ievadi skaitli: "))
    mazakais = skaitlis
    lielākais = skaitlis

    for i in range(daudzums - 1):
        skaitlis = int(input("Ievadi skaitli: "))

        if skaitlis < mazakais:
            mazakais = skaitlis

        if skaitlis > lielakais:
            lielakais = skaitlis

    print("Mazakais:",mazakais)
    print("Lielakais:", lielakais)