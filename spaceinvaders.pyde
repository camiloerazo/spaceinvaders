import random

def setup():
    size(1000,600)
    
class Enemigo:
    
        x = 0
        y = 0
        muerto = False
        
        def dibujar(s):
            if s.muerto == False:
                ellipse(s.x,s.y,30,30)    

matriz_enemigos = []#primero hacer un arreglo o matriz de enemigos
y = 70
for i in range(5):
    fila_de_enemigos = []
    x = 100
    for j in range(11):
        enemigo = Enemigo()
        enemigo.x = x
        enemigo.y = y
        fila_de_enemigos.append(enemigo)
        x += 50
    y += 50
    matriz_enemigos.append(fila_de_enemigos) 

class Disparo:
    
    x = 50
    y = 50
    cant_pasos_disparo = 550
    
    def dibujar(s):
        rect(s.x,s.y,7,40)

class Nave:
    
    x = 500
    y = 550
    tamano = 30
    velocidad = 10
    disparo = False
    
    def dibujar(s):
        square(s.x,s.y,s.tamano)
        
arreglo_disparos = []
ultima_ejecucion = 100000000
modo = "vivo"
vidas = 3
def keyPressed():
    
    global ultima_ejecucion,modo, vidas 
    
    if key == 'a':
        nave.x -= nave.velocidad
    elif key == 'd':
        nave.x += nave.velocidad
    elif key == ' ' and abs(millis() - ultima_ejecucion)>500:
        nave.disparo = True
        disparo = Disparo()
        disparo.x = nave.x + 15
        disparo.y = nave.y
        arreglo_disparos.append(disparo)
        ultima_ejecucion = millis()
    elif key == 'k':
        modo = "vivo"
        vidas = 3
        print("presione la tecla k")
        print("el modo despueps de presionar k es igual a ", modo)
        
nave = Nave()
disparo = Disparo()
ultimo_cambio = 10000000000
ultimo_cambio_disparos_random = 10000000000
direccion = "derecha"
cambios_de_direccion = 0
variable_para_girar = 100
arreglo_disparos_enemigos = []

def draw():
    global ultimo_cambio,direccion,cambios_de_direccion,variable_para_girar,ultimo_cambio_disparos_random
    global arreglo_disparos_enemigos, vidas, modo
    if modo == "vivo":
        background(0)
        texto = "Vidas " + str(vidas)
        text(texto,100,500,100)
        nave.dibujar()
        if nave.disparo == True: #me dice que hay disparos en el aire
            for disparo in arreglo_disparos:
                disparo.dibujar()
                for i in range(len(matriz_enemigos)):
                    x = matriz_enemigos[i]
                    for j in range(len(x)):
                        enemigo = matriz_enemigos[i][j]
                        if abs(enemigo.x - disparo.x) <20 and abs(enemigo.y - disparo.y) < 20:
                            enemigo.muerto = True
                            enemigo.x = 1001
                            enemigo.y = 601
                            arreglo_disparos.remove(disparo)
                            
                disparo.y -= 5
                disparo.cant_pasos_disparo -= 4
                if disparo.cant_pasos_disparo < 0:
                    #print(arreglo_disparos)
                    #print("se metio al remove")
                    arreglo_disparos.remove(disparo)
                    #print(arreglo_disparos)
                if len(arreglo_disparos) == 0:
                    #print("se metio al poner disparo en false")
                    nave.disparo = False
        
        for i in range(len(matriz_enemigos)):
            for j in range(len(matriz_enemigos[i])):
                enemigo = matriz_enemigos[i][j]
                enemigo.dibujar()
                
        
        if abs(millis() - ultimo_cambio) >500:
            for i in range(len(matriz_enemigos)):
                for j in range(len(matriz_enemigos[i])):
                        #print(enemigo.x)
                    if variable_para_girar >= 1700:
                        direccion = "izquierda"
                        cambios_de_direccion += 1
                    elif variable_para_girar <= 0:
                        direccion = "derecha"
                        cambios_de_direccion += 1
                    enemigo = matriz_enemigos[i][j]
                    if direccion == "derecha":
                        enemigo.x += 20
                        
                    elif direccion == "izquierda":
                        enemigo.x -= 20
                if direccion == "derecha":
                    variable_para_girar += 20
                elif direccion == "izquierda":
                    variable_para_girar -= 20
            ultimo_cambio = millis()
    
        if cambios_de_direccion % 2 == 0 and cambios_de_direccion != 0:
            #rint(cambios_de_direccion)
            #print("entre a cambios de direccion")
            for i in range(len(matriz_enemigos)):
                for j in range(len(matriz_enemigos[i])):
                    enemigo = matriz_enemigos[i][j]
                    enemigo.y += 30
            cambios_de_direccion = 0
        
        #Ahora se va a atrabajar en los disparos aleatorios de los enemigos, primero los 
        #no dirigidos
        if abs(ultimo_cambio_disparos_random - millis()) > 1000:
            #print("entre al if de los disparos random")
            while True:
                fila_aleatoria = random.randint(0,4)
                columna_aleatoria = random.randint(0,10)
                enemigo = matriz_enemigos[fila_aleatoria][columna_aleatoria]
                if enemigo.muerto == False:
                    break
            disparo = Disparo()
            disparo.x = enemigo.x
            disparo.y = enemigo.y
            arreglo_disparos_enemigos.append(disparo)
            
            ultimo_cambio_disparos_random = millis()
        len_disparos = len(arreglo_disparos_enemigos)  
        if len_disparos >= 1:
                for disparo in arreglo_disparos_enemigos:
                    c_nave_x = nave.x + 15 
                    c_nave_y = nave.y + 15
                    c_disparo_x = disparo.x + 3
                    c_disparo_y = disparo.y + 40
                    if abs(c_nave_x - c_disparo_x )< 15 and abs(c_nave_y -c_disparo_y)<15:
                        ellipse(nave.x,nave.y,20,20)
                        vidas -= 1
                        arreglo_disparos_enemigos.remove(disparo)
                    disparo.dibujar()
                    if disparo.y == 600:
                        arreglo_disparos_enemigos.remove(disparo)
                    disparo.y += 5
    if vidas == 0:
        modo = "muerto"
    if modo == "muerto":
        background(0)
        textSize(100)
        text("Perdiste",200,300)
        textSize(50)
        text("Presiona K para continuar",200,450)
