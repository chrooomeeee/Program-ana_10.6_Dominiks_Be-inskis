pareiza_parole = "6767"  # Saglabājam kā tekstu
meginajumi = 3

while meginajumi > 0:
    parole = input("Ievadiet paroli: ")

    if parole == pareiza_parole:
        print("Tu iegāji pa durvīm!")
        break  # Izejam no cikla, jo parole ir pareiza
    else:
        meginajumi -= 1  # Samazina atlikušos mēģinājumus par 1
        if meginajumi > 0:
            print(
                f"Nepareiza parole! Atlikuši {meginajumi} mēģinājumi."
            )

if meginajumi == 0:
    print("Piekļuve bloķēta! Mēģinājumi ir beigušies.")