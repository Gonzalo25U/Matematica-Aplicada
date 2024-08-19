def latencia():
    lat_estimada = int(input("ingrese la latencia estimada: "))
    lat_real = (lat_estimada * 120)/100 
    print(f"la latencia real es {lat_real}")



def cable_en_horas():
    #d=t/v*100
    tiempo = float(input("ingrese la cantidad de horas: "))
    distancia = round(tiempo/1.85 * 100 ,3)
    print(f"la distancia recorrida fue: {distancia} kilometros")
    
cable_en_horas()   

def cable_en_distancia():
    dist=float(input("ingrese la cantidad kilometros: "))
    tiemp= round(dist * 1.85 ,4)
    print(f"Han trabajado {tiemp} horas")
    
cable_en_distancia()