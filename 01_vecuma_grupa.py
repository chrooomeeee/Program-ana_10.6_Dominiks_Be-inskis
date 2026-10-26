print("Vecuma grupa")

vecums = int(input("Ievadi savu vecumu: "))

# Vecuma grupas noteikšana
if vecums < 6:
    grupa = "bērns"
elif vecums < 18:
    grupa = "pusaudzis"
elif vecums <= 18:
    grupa = "pieaugušais"
elif vecums > 40:
    grupa = "seniors"

print(f"Vecuma grupa ir: {grupa}")
