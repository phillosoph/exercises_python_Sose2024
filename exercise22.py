def teilbar(x, y): 
        if x%y == 0 :
            print("x ist durch y teilbar")
        else: 
            print("x ist nicht durch y teilbar") 
            
teilbar(19, 5)

def teilbar2(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x == y:
        print("x und y sind gleich")
    elif x%y == 0:
        print("x ist durch y teilbar")
    else:
        print("x ist nicht durch y teilbar")
        
        
teilbar2(10, 0)


