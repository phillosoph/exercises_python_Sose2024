test = "Hallo, Berlin"

letter_count = 0

for lol in test:
    if lol.isalpha():
        letter_count += 1
        
print(letter_count)
        
#oder

def buchstaben_zählen(wort):
    liste = list(wort)
    buchstabe = [i for i in liste if i.isalpha()]
    print(len(buchstabe))
    
buchstaben_zählen("Hallo, Berlin")

