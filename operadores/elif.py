
ingreso_mensual_dolares = 2500

if ingreso_mensual_dolares > 5000:
    print("Podes vivir en cualquier parte del mundo")
    
elif ingreso_mensual_dolares > 1000: #es como el else if de js. pero se escribe "elif"
    print("podes vivir en latinoamerica")
    
else:
    print("estudia python")
    
#if anidados
ingreso_mensual = 2500
gasto_mensual = 3500

if ingreso_mensual > 1500:
    if ingreso_mensual > gasto_mensual:
        print("podes gastar tranqui, pero ahorrá")
    
    elif ingreso_mensual == gasto_mensual:
        print("ojoooo, estas al limite")
    
    else:           
        print("estas en deficit y no te alcanza")
    
