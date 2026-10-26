try:
    n = int(ievade)
except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis vai ir tukša!")
    return

# 4. Paskaidro kļūdu, ja ievadīts 0 vai negatīvs skaitlis
if n <= 0:
    print(f"Kļūda: Skaitlim jābūt pozitīvam (lielākam par 0)! Jūs ievadījāt: {n}")
    return

# 2. Aprēķina visu skaitļu summu no 1 līdz n ar ciklu
kopēja_summa = 0
for skaitlis in range(1, n + 1):
    kopēja_summa += skaitlis

# 3. Parāda gala summu
print(f"Summa no 1 līdz {n} ir: {kopēja_summa}")
