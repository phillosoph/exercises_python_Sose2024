def steigung_funktion(Liste):
    x1 = Liste[0]
    y1 = Liste[1]
    x2 = Liste[2]
    y2 = Liste[3]
    
    delta_x = x2-x1
    delta_y = y2-y1
   
    if delta_x == 0:
        print("Die Steigung ist nicht definiert.")
    else:
        steigung = delta_y / delta_x
        print(steigung)
        
steigung_funktion([2,3,2,4])

 

    
