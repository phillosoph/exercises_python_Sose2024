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
#    print(len(buchstabe))
    
buchstaben_zählen("Hallo, Berlin")

#Übung 2

def vokon_zählen(wort2):
    vokale = "aeiou"
    wort_lower = wort2.lower()
    
    bu =[e for e in wort_lower if e.isalpha()]
    vok = [k for k in wort_lower if k in vokale]
    
    print(f"Es gibt {len(vok)} Vokale und {len(bu) - len(vok)} Konsonanten.")

vokon_zählen("HIIIIl")






#def vokon_zählen(wort2):
 #   wort2 = wort2.lower()
 #   liste = list(wort2)
 #   Vokale = [e for e in liste if e.isalpha()]
  #  Konsonanten = [f for f in liste if f.isalpha()]
  #  print((len(Vokale))+(len(Konsonanten)))

#okon_zählen("Hallo Berlin")
    
