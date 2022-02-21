print ("Bienvenidos al portal de la Federacion Nacional de Cacaoteros.")
print ("Analicemos el terreno donde tienes previsto plantar cacao.")
veces = float (input("Ingrese la cantidad de terrenos a analizar "))
suma_precipitacion=0
suma_profundidad=0
sumamente=0
moderadamente=0
marginalmente=0
noapto=0
i=1
while(i <= veces):
    precipitacion = float (input ("Cuanto es la precipitacion anual promedio en tu region (en mm) "))
    profundidad = float(input ("Cuanto es la profundidad efectiva en el suelo (en cm) "))
    suma_precipitacion = suma_precipitacion + precipitacion
    suma_profundidad = suma_profundidad + profundidad
    if (1800 <= precipitacion <=2599) and (profundidad > 100):
        sumamente = sumamente + 1
    elif (1800 <= precipitacion <=2599) and (50 <= profundidad <= 100):
        moderadamente = moderadamente + 1
    elif (1800 <= precipitacion <=2599) and (25 <= profundidad < 50):
        marginalmente = marginalmente + 1
    elif (1800 <= precipitacion <=2599) and (profundidad < 25):
        noapto = noapto + 1
    elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (profundidad > 50):
        moderadamente = moderadamente + 1
    elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (25 <= profundidad <= 50):
        marginalmente = marginalmente + 1
    elif ((2600 <= precipitacion <=3199)or(1500 <= precipitacion <=1799)) and (profundidad < 25):
        noapto = noapto + 1
    elif ((3200 <= precipitacion <=3800)or(1200 <= precipitacion <=1499)) and (profundidad >= 25):
        marginalmente = marginalmente + 1
    else:
        noapto = noapto + 1
    i+=1
promedio_precipitacion = round ((suma_precipitacion / veces),2)
promedio_profundidad = round ((suma_profundidad / veces),2)
print ("{:.2f}".format(promedio_precipitacion))
print ("{:.2f}".format(promedio_profundidad))
print("sumamente apto ",sumamente)
print("moderadamente apto ",moderadamente)
print("marginalmente apto ",marginalmente)
print("no apto ",noapto)