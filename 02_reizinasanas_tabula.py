# Fails: 02_reizinasanas_tabula.py

print("Reizināšanas tabula")

try:
    skaitlis = int(input("Ievadi veselu skaitli: "))
    
    # Izvada reizināšanas tabulu no 1 līdz 10
    for i in range(1, 11):
        rezultāts = skaitlis * i
        print(f"{skaitlis} x {i} = {rezultāts}")

except ValueError:
    print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu!")