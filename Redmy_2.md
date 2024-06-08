import random

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("La cola está llena")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("La cola está vacía")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def asignar_turnos(self, num_turnos):
        if self.front == -1:
            print("La cola está vacía")
        else:
            print("Asignando turnos:")
            for i in range(num_turnos):
                print("Turno", i + 1, ":", self.queue[i % self.size])
    
    def buscar_numero(self, numero):
        if self.front == -1:
            print("La cola está vacía")
            return False
        else:
            for i in range(self.size):
                if self.queue[i] == numero:
                    return i
            print("Número no encontrado en la cola")
            return False
    
    def display(self):
        if self.front == -1:
            print("La cola está vacía")
        elif self.rear >= self.front:
            print("Elementos de la cola:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Elementos de la cola:")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


jugadas={}
jugadas1={}
jugadas2={}
JugadasBot=[]
lista_de_fichasEval=[]

#se definen las listas que utilizaran los bots en la partida
lista_de_fichas = []
lista_de_fichasBot={}
lista_de_fichasBot[0]=[]
lista_de_fichasBot[1]=[]
lista_de_fichasBot[2]=[]
lista_de_fichasBot[3]=[]
lista_de_fichasBot[4]=[]
# es la lista en la cual se guardan todas las fichas disponibles del tablero en un instante
lista_de_fichasBotP=[]

#se define la lista que se utiliza para juntar todas las piezas disponibles tanto del tablero como del bot

lista_de_fichasBotFT=[]
jugadasLegales=[]

listas_de_tablero = []
#comprueba si el argumento es un valor numerico
def has_numeric_value(lst): 
    for item in lst: 
        if isinstance(item, (int)): 
            return True 
    return False 
def determinarJugadas(lista_de_fichasEval):
    #llevan la cuenta del color de las fichas, pero creo que no sirven para nada y las voy a borrar
    contN=0
    contV=0
    contA=0
    contR=0
    #son las listas en las que se guardan las fichas segun sus caracteristicas 
    fichaN=[]
    fichaR=[]
    fichaV=[]
    fichaA=[]
    fichaNo1=[]
    fichaNo2=[]
    fichaNo3=[]
    fichaNo4=[]
    fichaNo5=[]
    fichaNo6=[]
    fichaNo7=[]
    fichaNo8=[]
    fichaNo9=[]
    fichaNo10=[]
    fichaNo11=[]
    fichaNo12=[]
    fichaNo13=[]
    fichaNo14=[]
    
    #empieza la categorizacion y se ordenan
    for element in (lista_de_fichasEval):
        if (element.cadena == 'N'):
            contN=contN+1
            fichaN.append(element.numero1)
            fichaN.sort()
            
            
        
        if (element.cadena== 'R'):
            contR=contR+1
            fichaR.append(element.numero1)
            fichaR.sort()
        if (element.cadena== 'A'):
            contA=contA+1
            fichaA.append(element.numero1)
            fichaA.sort()
        if (element.cadena== 'V'):
            contV=contV+1
            fichaV.append(element.numero1)
            fichaV.sort()
        if (element.numero1==1):
                fichaNo1.append(element.cadena)
                
        if (element.numero1==2):
                fichaNo2.append(element.cadena)
            
        if (element.numero1==3):
                fichaNo3.append(element.cadena)
            
        if (element.numero1==4):
                fichaNo4.append(element.cadena)
            
        if (element.numero1==5):
                fichaNo5.append(element.cadena)
        
        if (element.numero1==6):
                fichaNo6.append(element.cadena)
            
        if (element.numero1==7):
                fichaNo7.append(element.cadena)
            
        if (element.numero1==8):
                fichaNo8.append(element.cadena)
                
        if (element.numero1==9):
                fichaNo9.append(element.cadena)
                
        if (element.numero1==10):
                fichaNo10.append(element.cadena)
            
        if (element.numero1==11):
                fichaNo11.append(element.cadena)
            
        if (element.numero1==12):
                fichaNo12.append(element.cadena)
            
        if (element.numero1==13):
                fichaNo13.append(element.cadena)
                
        if (element.numero1==14):
                fichaNo14.append(element.cadena)
    
    
    JugadasBot=[]
    #ya que queremos que se vacie la lista de jugadas y el argumento, se vacian tras cada llamada a la funcion
    jugadasLegales=[]
    #se reciben como argumentos las listas de categorias de fichas y el identificador de estas
    def posiblesJugadasBot(JugadasBot, JugadasBotName):
        # las listas en donde se guardan las jugadas en base a las busqueda en la que se encontraron, 
        # si fue por color o numero, se toma en cuenta el maximo de jugadas posibles
        jugadasc={}
        jugadas1c={}
        jugadas2c={}
        jugadasnameS=JugadasBotName
        jugadasn={}
        jugadasLegales=[]
        #se inicializan las listas para las jugadas en base a la caracteristica principal de las fichas
        for JugadasBotName in ['N', 'R', 'V', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
            jugadasc[JugadasBotName] = []
            jugadas1c[JugadasBotName] = []
            jugadas2c[JugadasBotName] = []
            jugadasn[JugadasBotName] = []
        JugadasBotName=jugadasnameS
        for i in range (len(JugadasBot)):
            if (has_numeric_value(JugadasBot)==True and len(JugadasBot)>0):
            
                
               #se van a llenar las listas una tras de otra, nunca se abrira la lista 2 a menos que la 
               # lista 1 este llena
               # si esta vacia, siempre entrara la ficha
                if (len(jugadasc[JugadasBotName])==0):
                    jugadasc[JugadasBotName].append(JugadasBot[i])
                    condicion=1
                   # se comprueba si es sucesor
                if (len (jugadasc[JugadasBotName]) >0 and jugadasc[JugadasBotName][-1]==JugadasBot[i]-1 ):
                    jugadasc[JugadasBotName].append(JugadasBot[i])
                  # si no lo es ni es igual, se vacia la lista si es que no cumple con el tamaño minimo
                if (jugadasc[JugadasBotName][-1]!=JugadasBot[i]-1 and jugadasc[JugadasBotName][-1]!=JugadasBot[i] and len(jugadasc[JugadasBotName])<3 and condicion==0):
                   
                    for w in range (0,len(jugadasc[JugadasBotName])):
                        
                        jugadasc[JugadasBotName].pop()
                #se comienza a llenar la siguiente lista si aun faltan elementos por revisar
                if (len(jugadasc[JugadasBotName])>0 and jugadasc[JugadasBotName][-1]!=JugadasBot[i]):
                    
                    if (len(jugadas1c[JugadasBotName])==0):
                            jugadas1c[JugadasBotName].append(JugadasBot[i])
                            
                    if (jugadas1c[JugadasBotName][-1]==JugadasBot[i]-1):
                            jugadas1c[JugadasBotName].append(fichaN[i])
                    if (jugadas1c[JugadasBotName][-1]!=JugadasBot[i]-1 and len(jugadas1c[JugadasBotName])<3):
                            for j in range (0,len(jugadas1c[JugadasBotName])):
                                jugadas1c[JugadasBotName].pop()
                
                if (len(jugadasc[JugadasBotName])>0 and jugadasc[JugadasBotName][-1]!=JugadasBot[i] and len(jugadas1c[JugadasBotName])>0 and jugadas1c[JugadasBotName][-1]!=JugadasBot[i]):
                    
                    if (len(jugadas2c[JugadasBotName])==0):
                            jugadas2c[JugadasBotName].append(JugadasBot[i])
                    if (jugadas2c[JugadasBotName][-1]==JugadasBot[i]-1):
                            jugadas2c[JugadasBotName].append(JugadasBot[i])
                    if (jugadas2c[JugadasBotName][-1]!=JugadasBot[i]-1 and len(jugadas2c[JugadasBotName][-1])<3):
                            for j in range (0,len(jugadas2c[JugadasBotName])):
                                jugadas2c[JugadasBotName].pop()
                condicion=0
            
                
                #se revisan las listas de las fichas que comparten el mismo numero, el identificador es el color
            if (has_numeric_value(JugadasBot)==False and len(JugadasBot)>0):
                
            
                if (len(jugadasn[JugadasBotName])==0):
                    jugadasn[JugadasBotName].append(JugadasBot[i])
                    #se debe de comprobar cada vez si es que el elemento no esta ya en la lista
                for element in range (len(jugadasn[JugadasBotName])):
                    if (jugadasn[JugadasBotName][-element]==JugadasBot[i]):
                        condicion2a = 0
                if (condicion2a != 0):
                    jugadasn[JugadasBotName].append(JugadasBot[i])
                condicion2a = 1
                if (len(jugadasn[JugadasBotName])<3 and jugadasn[JugadasBotName][-1]!=JugadasBot[i]):

                    for j in range (0,len(jugadasn[JugadasBotName])):
                        
                        jugadasn[JugadasBotName].pop()
            
            #si es que las listas alcanzan el tamaño minimo, entonces se guardan como jugadas legales
        if (len(jugadasc[JugadasBotName])>2):
            jugadasc[JugadasBotName].append(JugadasBotName)
            jugadasLegales.append(jugadasc[JugadasBotName])
            
        if (len(jugadas1c[JugadasBotName])>2):
            jugadas1c[JugadasBotName].append(JugadasBotName)
            jugadasLegales.append(jugadas1c[JugadasBotName])
        
        if (len(jugadas2c[JugadasBotName])>2):
            jugadas2c[JugadasBotName].append(JugadasBotName)
            jugadasLegales.append(jugadas2c[JugadasBotName])
        
        if (len(jugadasn[JugadasBotName])>2):
            jugadasn[JugadasBotName].append(JugadasBotName)
            jugadasLegales.append(jugadasn[JugadasBotName])
            
                    
        return jugadasLegales
    #aqui se esta llamando a la funcion para evaluarla con las listas de todas las categorias
    jugadasLegales.extend(posiblesJugadasBot(fichaN, "N"))
    jugadasLegales.extend(posiblesJugadasBot(fichaR, "R"))
    jugadasLegales.extend(posiblesJugadasBot(fichaV, "V"))
    jugadasLegales.extend(posiblesJugadasBot(fichaA, "A"))

    jugadasLegales.extend(posiblesJugadasBot(fichaNo1, "1"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo2, "2"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo3, "3"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo4, "4"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo5, "5"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo6, "6"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo7, "7"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo8, "8"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo9, "9"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo10, "10"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo11, "11"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo12, "12"))
    jugadasLegales.extend(posiblesJugadasBot(fichaNo13, "13"))




   
    #if (len(jugadasLegales)>0):
        #print(jugadasLegales)
      
    #print(len(lista_de_fichas))
    return jugadasLegales    

jugadasLegales=determinarJugadas(lista_de_fichasBot[0])  


class Ficha:
    def __init__(self, cadena, numero1, numero2):
        self.cadena = cadena
        self.numero1 = numero1
        self.numero2 = numero2

    def __str__(self):
        return f"Ficha: Color='{self.cadena}', Numero1={self.numero1}, Numero2={self.numero2}"
        

def generar_fichas_por_color(color):
    fichas = [Ficha(color, numero, random.randint(1, 1000)) for numero in range(1, 14)]
    return fichas

def generar_lista_de_fichas():
    colores = ["R", "A", "V", "N"]
    lista_de_listas = []
    for color in colores:
        sublistas_por_color = [generar_fichas_por_color(color) for _ in range(2)]
        lista_de_listas.extend(sublistas_por_color)  
    return lista_de_listas

#Aquí simplemente hice función lo que había mandado antes, la explicación está en whats
def Generar_pozo_de_fichas():
    lista_de_fichas = generar_lista_de_fichas()

    fichas_combinadas = [ficha for sublist in lista_de_fichas for ficha in sublist]

    fichas_combinadas_ordenadas = sorted(fichas_combinadas, key=lambda ficha: ficha.numero2, reverse=True)

    pila_de_fichas = []

    for ficha in fichas_combinadas_ordenadas:
        pila_de_fichas.append(ficha)

    return pila_de_fichas

#Si no encuentra la pila menciona que está vacía, en caso contrario hace un pop a la pila y regresa lo que tomó
def sacar_ficha_de_pila(pila):
    if not pila:
        print("La pila está vacía, no hay fichas para sacar.")
        return None
    else:
        ficha = pila.pop()
        return ficha

#Generamos el pozo de fichas en una pila
mi_pozo_de_fichas = Generar_pozo_de_fichas()

lista_de_fichas = []


listas_de_tablero = []

r = 0

turnos_bot_completados = 0

print("Rummy")
print()
print()
print("Repartiendo fichas del pozo...")
for i in range (13):
    ficha_sacada = sacar_ficha_de_pila(mi_pozo_de_fichas)
    lista_de_fichas.append(ficha_sacada)
print("Fichas sacadas: ")
for i, ficha in enumerate(lista_de_fichas):
    print(f"{i+1}. {ficha.cadena}{ficha.numero1}")
print()

players = int(input("¿Cuántos bots hay en la partida? "))
turnos = CircularQueue(players + 1)

#se generan los mazos de los bots con los que se va a jugar
for y in range(players+1):
    for k in range(13):
         FichasJ=sacar_ficha_de_pila(mi_pozo_de_fichas) 
         lista_de_fichasBot[y].append(Ficha(FichasJ.cadena, FichasJ.numero1, FichasJ.numero2))
for i in range(players + 1):
    turnos.enqueue(i + 1)
turnos.display()
print("Asignando turnos...")
turno_jugador = random.randint(1, players + 1)
print(f"El turno del jugador es: {turno_jugador}")

while True:
    turno_actual = turnos.dequeue()
    
    if turno_actual == turno_jugador:
        print("¡Es el turno del jugador humano!")
        
        while True:
            
            tablero = []
            if len(listas_de_tablero)==0:
                Puntos = 0
                print("¿Desea agregar fichas al tablero, o come una ficha y pasa turno?")
                respuesta = input("Ingrese 'a' para agregar, 'c' para comer: ")
            
            else:
                print("¿Desea agregar fichas al tablero, modificar alguna jugada, comer una ficha o terminar el programa?")
                respuesta = input("Ingrese 'a' para agregar, 'm' para modificar alguna jugada, 'c' para comer o 'n' para salir: ")
        
            if (respuesta.lower() == 'a'):
                print("Fichas disponibles para agregar:")
                for i, ficha in enumerate(lista_de_fichas):
                    print(f"{i+1}. {ficha.cadena}{ficha.numero1}")
                    
                fichas_a_agregar = input("\nIngrese la posición de las fichas que desea agregar separados por comas (por ejemplo, '1, 3, 4'): ")
                indices_fichas = [int(idx) - 1 for idx in fichas_a_agregar.split(',')]
        
                indices_fichas_agregadas = []
        
                for idx in indices_fichas:
                    if 0 <= idx < len(lista_de_fichas):
                        if len(tablero) == 0 or \
                        (lista_de_fichas[idx].numero1 == tablero[-1].numero1 + 1 and lista_de_fichas[idx].cadena == tablero[-1].cadena) or \
                        (lista_de_fichas[idx].numero1 == tablero[-1].numero1 and lista_de_fichas[idx].cadena not in [ficha.cadena for ficha in tablero] and \
                        (lista_de_fichas[idx].numero1 - 1 not in [ficha.numero1 for ficha in tablero] and lista_de_fichas[idx].numero1 + 1 not in [ficha.numero1 for ficha in tablero])):
        
                            tablero.append(lista_de_fichas[idx])
                            indices_fichas_agregadas.append(idx)
                            print(f"Ficha {idx+1} agregada al tablero.")
                            if (r == 0):
                                Puntos += lista_de_fichas[idx].numero1
                        else:
                            print(f"No se puede agregar la ficha {idx+1}. No está cumpliendo con alguna de las reglas.")
                    else:
                        print(f"Índice {idx+1} fuera de rango. Ignorado.")
        
                if (r != 0 and len(tablero) >= 3) or (r == 0 and len(tablero) >= 3 and Puntos >= 30):              
                    print("\nLa jugada es válida.")
                    print("Nueva jugada: ", end = "")
                    c = 0
                    for ficha in tablero:
                        if c != 0:
                            print("-", end = "")
                        print(f"{ficha.cadena}{ficha.numero1}", end="")
                        c = c + 1
                    print("\n\nFichas disponibles para agregar:")
                    for i, ficha in enumerate(lista_de_fichas):
                        if i!=0:
                            print(", ", end = "")
                        print(f"{ficha.cadena}{ficha.numero1}", end="")
        
                    listas_de_tablero.append(tablero)
                else:
                    print("La jugada no es válida. Se requieren al menos 3 fichas en el tablero.")
            
            elif respuesta == 'm':
                
                print("Jugadas formadas hasta el momento:")
                for i, lista in enumerate(listas_de_tablero):
                    print(f"Jugada {i+1}:", end = " ")
                    c = 0
                    for ficha in lista:
                        if c != 0:
                            print("-", end = "")
                        print(f"{ficha.cadena}{ficha.numero1}", end="")
                        c = c + 1
                    print()
                print("\n\nFichas disponibles para agregar:")
                for i, ficha in enumerate(lista_de_fichas):
                    if i!=0:
                        print(", ", end = "")
                    print(f"{ficha.cadena}{ficha.numero1}", end="")
                print("\n\nOpciones de modificación:")
                print("1) Agregar fichas adicionales a alguna jugada")
                print("2) Intercambiar fichas en alguna jugada")
                print("3) Tomar fichas de alguna jugada")
                opcion_modificacion = input("Ingrese el número de la opción que desea realizar: ")
        
                if opcion_modificacion == '1':
                    print("\nJugadas formadas hasta el momento:")
                    for i, lista in enumerate(listas_de_tablero):
                        print(f"Jugada {i+1}:", end = " ")
                        c = 0
                        for ficha in lista:
                            if c != 0:
                                print("-", end = "")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            c = c + 1
                        print()
        
                    num_jugada = int(input("\nIngrese el número de la jugada que desea modificar: "))
            
                    if 1 <= num_jugada <= len(listas_de_tablero):
                        indices_fichas_agregadas = []
                        jugada_seleccionada = listas_de_tablero[num_jugada - 1]
                        print("Jugada seleccionada:")
                        c = 0
                        for ficha in jugada_seleccionada:
                            if c != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            c = c+1
                        print()
                        print("Fichas disponibles para agregar:")
                        for i, ficha in enumerate(lista_de_fichas):
                            print(f"{i+1}. {ficha.cadena}{ficha.numero1}")
                        fichas_a_agregar = input("\nIngrese el número de las fichas que desea agregar separadas por comas (por ejemplo, '1, 3, 4'): ")
                        indices_fichas = [int(idx) - 1 for idx in fichas_a_agregar.split(',')]
                
                        for idx in indices_fichas:
                            if 0 <= idx < len(lista_de_fichas):
                                nueva_ficha = lista_de_fichas[idx]
                                if (nueva_ficha.numero1 == jugada_seleccionada[-1].numero1 + 1 and nueva_ficha.cadena == jugada_seleccionada[-1].cadena):
                                    jugada_seleccionada.append(nueva_ficha)
                                    print(f"Ficha {nueva_ficha.cadena}{nueva_ficha.numero1} agregada al final de la jugada.")
                                    indices_fichas_agregadas.append(idx)
                                    
                                elif (nueva_ficha.numero1 == jugada_seleccionada[0].numero1 - 1 and nueva_ficha.cadena == jugada_seleccionada[0].cadena):
                                    jugada_seleccionada.insert(0, nueva_ficha)
                                    print(f"Ficha {nueva_ficha.cadena}{nueva_ficha.numero1} agregada al inicio de la jugada.")
                                    indices_fichas_agregadas.append(idx)
                                    
                                elif (lista_de_fichas[idx].numero1 == jugada_seleccionada[-1].numero1) and \
                                (lista_de_fichas[idx].cadena not in [ficha.cadena for ficha in jugada_seleccionada]) and \
                                ((lista_de_fichas[idx].numero1 - 1 not in [ficha.numero1 for ficha in jugada_seleccionada]) or \
                                (lista_de_fichas[idx].numero1 + 1 not in [ficha.numero1 for ficha in jugada_seleccionada])):
                                    jugada_seleccionada.append(nueva_ficha)
                                    indices_fichas_agregadas.append(idx)
        
                                else:
                                    print(f"No se puede agregar la ficha {nueva_ficha.cadena}{nueva_ficha.numero1}. No cumple las condiciones.")
                            else:
                                print(f"Índice {idx+1} fuera de rango. Ignorado.")
        
                        for idx in sorted(indices_fichas_agregadas, reverse=True):
                            lista_de_fichas.pop(idx)
                        print("Jugada actualizada:")
                        c = 0
                        for ficha in jugada_seleccionada:
                            if c != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            c = c + 1
                        print()
            
                    else:
                        print("Número de jugada no válido.")
                elif opcion_modificacion == '2':
                    print("\nJugadas formadas hasta el momento:")
                    for i, lista in enumerate(listas_de_tablero):
                        print(f"Jugada {i+1}:", end=" ")
                        for j, ficha in enumerate(lista):
                            if j != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                        print()
        
                    num_jugada = int(input("\nIngrese el número de la jugada que desea modificar: "))
        
                    if 1 <= num_jugada <= len(listas_de_tablero):
                        jugada_seleccionada = listas_de_tablero[num_jugada - 1]
                        print("Jugada seleccionada:")
                        for i, ficha in enumerate(jugada_seleccionada):
                            if i != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                        print()
        
                        indice_ficha_a_intercambiar = int(input("\nIngrese la posición de la ficha que desea intercambiar en la jugada seleccionada: ")) - 1
                        if 0 <= indice_ficha_a_intercambiar < len(jugada_seleccionada):
                            ficha_seleccionada = jugada_seleccionada[indice_ficha_a_intercambiar]
        
                            print("Fichas disponibles para agregar:")
                            for i, ficha in enumerate(lista_de_fichas):
                                print(f"{i+1}. {ficha.cadena}{ficha.numero1}")
        
                            indice_ficha_disponible = int(input("\nIngrese la posición de la ficha disponible que desea agregar: ")) - 1
                            if 0 <= indice_ficha_disponible < len(lista_de_fichas):
                                nueva_ficha = lista_de_fichas[indice_ficha_disponible]
                                
                                if (nueva_ficha.numero1 == ficha_seleccionada.numero1 and nueva_ficha.cadena == ficha_seleccionada.cadena) or \
                                (nueva_ficha.numero1 == ficha_seleccionada.numero1 and nueva_ficha.cadena not in [ficha.cadena for ficha in jugada_seleccionada]):
                                    jugada_seleccionada.pop(indice_ficha_a_intercambiar)
                                    lista_de_fichas.pop(indice_ficha_disponible)
                                    jugada_seleccionada.insert(indice_ficha_a_intercambiar, nueva_ficha)
                                    print(f"Ficha {ficha_seleccionada.cadena}{ficha_seleccionada.numero1} intercambiada por {nueva_ficha.cadena}{nueva_ficha.numero1} en la jugada.")
                                    lista_de_fichas.append(ficha_seleccionada)
                                else:
                                    print("No es posible agregar la ficha seleccionada a la jugada")
                            else:
                                print("Índice de ficha disponible fuera de rango. No se realizó el intercambio.")
                        else:
                            print("Índice de ficha seleccionada fuera de rango.")
                    else:
                        print("Número de jugada no válido.")
        
                elif opcion_modificacion == '3':
                    print("\nJugadas formadas hasta el momento:")
                    for i, lista in enumerate(listas_de_tablero):
                        print(f"Jugada {i+1}:", end=" ")
                        c = 0
                        for ficha in lista:
                            if c != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            c = c + 1
                        print()
        
                    num_jugada = int(input("Ingrese el número de la jugada de la que desea tomar una ficha: "))
        
                    if 1 <= num_jugada <= len(listas_de_tablero):
                        jugada_seleccionada = listas_de_tablero[num_jugada - 1]
                        if len(jugada_seleccionada) > 3:
                            print("Jugada seleccionada:")
                            for i, ficha in enumerate(jugada_seleccionada):
                                if i != 0:
                                    print("-", end="")
                                print(f"{ficha.cadena}{ficha.numero1}", end="")
                            print()
                            if len(set(ficha.numero1 for ficha in jugada_seleccionada)) > 1:
                                print("¿Desea tomar la primera ficha o la última ficha de la jugada?")
                                print("1) Primera ficha")
                                print("2) Última ficha")
                                opcion = input("Ingrese el número de la opción que desea realizar: ")
        
                                if opcion == '1':
                                    ficha_quitada = jugada_seleccionada.pop(0)
                                    lista_de_fichas.append(ficha_quitada)
                                    print(f"Ficha {ficha_quitada.cadena}{ficha_quitada.numero1} tomada de la jugada y devuelta a las fichas disponibles.")
                                elif opcion == '2':
                                    ficha_quitada = jugada_seleccionada.pop()
                                    lista_de_fichas.append(ficha_quitada)
                                    print(f"Ficha {ficha_quitada.cadena}{ficha_quitada.numero1} tomada de la jugada y devuelta a las fichas disponibles.")
                                else:
                                    print("Opción no válida.")
                            else:
                                opcion = int(input("Ingrese la posición de la ficha que desea quitar: ")) - 1
                                ficha_quitada = jugada_seleccionada.pop(opcion)
                                lista_de_fichas.append(ficha_quitada)
                                print(f"Ficha {ficha_quitada.cadena}{ficha_quitada.numero1} tomada de la jugada y devuelta a las fichas disponibles.")
                        else:
                            print("La jugada debe tener al menos 4 fichas para poder quitar una.")
                    else:
                        print("Número de jugada no válido.")
        
                else:
                    print("Opción no válida.")
                    
            elif (respuesta.lower() == 'c'):
                ficha_sacada = sacar_ficha_de_pila(mi_pozo_de_fichas)
        
                if ficha_sacada is not None:
                    lista_de_fichas.append(ficha_sacada)
                    print(f"\nFicha sacada: {ficha_sacada.cadena}{ficha_sacada.numero1}")
                else:
                    print("¡¡¡Ya no hay fichas en el pozo!!!")
                print()
                
                print("Pasa el turno")
                turnos.enqueue(turno_actual)
                break
                
        
            elif (respuesta.lower() == 'n'):
                turnos.enqueue(turno_actual)
                print("Siguiente turno")
                break 
            else:
                print("Respuesta no válida. Programa terminado.")
                break 
            if(len(listas_de_tablero) != 0):
                print("\nJugadas formadas hasta el momento:")
                for i, lista in enumerate(listas_de_tablero):
                    print(f"Jugada {i+1}:", end = " ")
                    c = 0
                    for ficha in lista:
                        if c != 0:
                            print("-", end = "")
                        print(f"{ficha.cadena}{ficha.numero1}", end="")
                        c = c + 1
                    print()
            else:
                print("No hay jugadas hasta el momento")
                
            if (respuesta.lower() != 'c'):
                if (len(listas_de_tablero) > 0):
                    continuar = input("\n\nDesea hacer otra jugada? (Ingrese 's' para Sí, 'n' para No): ")
                    r = r + 1
                    if continuar.lower() != 's':
                        turnos.enqueue(turno_actual)
                        print("Siguiente turno")
                        break 
                else:
                    print("\n\nNo se han agregado jugadas al tablero, debe agregar una jugada o en su defecto comer una ficha\n")
                    continuar = input("\n\nDesea hacer otra jugada? (Ingrese 's' para Sí, 'c' para comer): ")
                    
                    if continuar.lower() == 'c':
                        ficha_sacada = sacar_ficha_de_pila(mi_pozo_de_fichas)
        
                        if ficha_sacada is not None:
                            lista_de_fichas.append(ficha_sacada)
                            print(f"\nFicha sacada: {ficha_sacada.cadena}{ficha_sacada.numero1}")
                        else:
                            print("¡¡¡Ya no hay fichas en el pozo!!!")
                        print()
                
                        print("Pasa el turno")
                        turnos.enqueue(turno_actual)
                        break
                    
    else:
        print("Turno del bot:", turno_actual)
        turnos.enqueue(turno_actual)
       
        print(f"num de fichas {len(lista_de_fichasBot[turno_actual-1])}")
    
    tablero=[]
    checkDeckLen=len(lista_de_fichasBot[turno_actual-1])
    #if (len(listas_de_tablero)==0):
    jugadasLegales=determinarJugadas(lista_de_fichasBot[turno_actual-1])
    
    
    
    listaPreferent=0
    # la lista preferente se planea que sea siempre la de mayor longitud
    if (len(jugadasLegales)>0):
        for p in range (0, len(jugadasLegales)-1):
            if (len(jugadasLegales[p])>len(jugadasLegales[listaPreferent])):
                listaPreferent=p

        p=listaPreferent
        shrC=jugadasLegales[p][-1]
        if (shrC=='N' or shrC=='A' or shrC=='R' or shrC=='V'):
            for element4 in (lista_de_fichasBot[turno_actual-1]):
                
                #se comienzan por revisar si alguna de las listas cuenta con las fichas de la jugada
            
                
                if (shrC=='N' or shrC=='A' or shrC=='R' or shrC=='V'):
                    for q in range (0, len(jugadasLegales[p])):
                    
                        if (len(jugadasLegales[p])>q and element4.cadena==shrC and element4.numero1 == jugadasLegales[p][q]):
                                tablero.append(element4)
                                jugadasLegales[p].remove(element4.numero1)
                                lista_de_fichasBot[turno_actual-1].remove(element4)
                                
                                
                            
                    
            if (len(jugadasLegales[p])==1):
                    listas_de_tablero.append(tablero)
                    
            
            for i, lista in enumerate(listas_de_tablero):
                        print(f"Jugada {i+1}:", end=" ")
                        c = 0
                        for ficha in lista:
                            if c != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            c = c + 1
                        print()
            
        else:
            
                # ahora se revisa en base a las que comparten el numero y tienen colores diferentes
            if (  len(jugadasLegales)>0):
                
                for element5 in (lista_de_fichasBot[turno_actual-1]):
                    
                    
                    # aqui se revisa primero el mazo, ya que no importa si se quita una ficha central de 
                    #alguna jugada del tablero
                    for q in range(len(jugadasLegales[p])-1):
                        
                        
                    
                        if (element5.numero1==shrC and element5.cadena == jugadasLegales[p][q]):
                                tablero.append(element5)
                                jugadasLegales[p].remove(element5.cadena)
                                element5.cadena.pop()
                                element5.numero1.pop()
                                print("1")
                                
                                
                            
            
            if (len(jugadasLegales[p])==1):
                listas_de_tablero.append(tablero)
                
                for i, lista in enumerate(listas_de_tablero):
                        print(f"Jugada {i+1}:", end=" ")
                        c = 0
                        for ficha in lista:
                            if c != 0:
                                print("-", end="")
                            print(f"{ficha.cadena}{ficha.numero1}", end="")
                            print("9")
                            c = c + 1
                        print()
         # si no se bajo ninguna ficha, automaticamente se come
        if (checkDeckLen==len(lista_de_fichasBot[turno_actual-1])):
            FichasJ=sacar_ficha_de_pila(mi_pozo_de_fichas) 
            lista_de_fichasBot[turno_actual-1].append(Ficha(FichasJ.cadena, FichasJ.numero1, FichasJ.numero2))
    else:
        while True:
            for x, lista in enumerate(listas_de_tablero):
            
            
                lista_de_fichasBotP.extend(lista)
                #se revisan las listas para obtener el numero de cartas maximo que se puede retirar
                # para garantizar que siempre se quedara al menos con 3
                SizeExtremos=len(lista_de_fichasBotP)-3
                for g in range (SizeExtremos):
                    # en este caso se estan añadiendo las fichas desde el extremo derecho, dejando fuera las
                    #3 primeras
                    # se juntan todas las fichas posibles y se obtienen las jugadas legales
                     
                    lista_de_fichasBotFT.extend([lista_de_fichasBotP[-g]])
                        
            lista_de_fichasBotFT.extend(lista_de_fichasBot[turno_actual-1])
            jugadasLegales=determinarJugadas(lista_de_fichasBotFT)
            listaPreferent=0
            # la lista preferente se planea que sea siempre la de mayor longitud
            if (len(jugadasLegales)>0):
                for p in range (0, len(jugadasLegales)-1):
                    if (len(jugadasLegales[p])>len(jugadasLegales[listaPreferent])):
                        listaPreferent=p

                p=listaPreferent
                if (len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        break
                print("y")
                contR=0
                #se comienzan por revisar si alguna de las listas cuenta con las fichas de la jugada
                for q in range(0, len(jugadasLegales[p])-2):
                    shrC=jugadasLegales[p][-1]
                    if (shrC=='N' or shrC=='A' or shrC=='R' or shrC=='V'):
                        condicion3=1
                        for n, lista in enumerate(listas_de_tablero):
                            if (SaveN!=n):
                                contR=0
                            SaveN=n
                            contR=+1
                            condicionrep=1
                            if (contR>3):
                                if (lista.cadena==shrC and lista.numero1 == jugadasLegales[p][q]):
                                        tablero.append(lista)
                                        jugadasLegales[p].remove(lista.numero1)
                                        lista.cadena.pop()
                                        lista.numero1.pop()
                                        print("x")
                                        condicion3=0
                                        condicionrep=0
                            # si no se encuentran las fichas, se busca en el mazo del bot
                            if (condicion3!=0):
                                for element2 in (lista_de_fichasBot[turno_actual-1]):
                                    if element2.cadena==shrC and element2.numero1 == jugadasLegales[p][q]:
                                        tablero.append(element2)
                                        jugadasLegales[p].remove(element2.numero1)
                                        element2.cadena.pop()
                                        element2.numero1.pop()
                                        print("2")
                                        condicionrep=0
                            if (condicionrep!=0):
                                n=0
                if (len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        break
            
            
            

            lista_de_fichasBotFT=[]
            # ahora se toman las fichas desde la izquierda, dejando las ultimas 3 fichas fuera, 
            # se hace si es que no se bajo ninguna ficha del mazo del bot
            if (  checkDeckLen==len(lista_de_fichasBot[turno_actual-1]) and (len(jugadasLegales))>0):
        
                for x, lista in enumerate(listas_de_tablero):
                
                    condicionrep=1
                    lista_de_fichasBotP.extend(lista)
                    SizeExtremos=len(lista_de_fichasBotP[-1])-3
                    for g in range (0, SizeExtremos-1):
                        for element1 in (lista_de_fichasBotP[g]):
                            lista_de_fichasBotFT.append(element1)
                            
                lista_de_fichasBotFT.extend(lista_de_fichasBot[turno_actual-1])
                jugadasLegales=determinarJugadas(lista_de_fichasBotFT)
                listaPreferent=0

                for p in range (0, len(jugadasLegales)-1):
                    if (len(jugadasLegales[p])>len(jugadasLegales[listaPreferent])):
                        listaPreferent=p

                p=listaPreferent
                if (len(jugadasLegales)<p and len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        break
                contR=0
                if (len(jugadasLegales)<p and len(jugadasLegales[p])==1):
                    listas_de_tablero.append(tablero)
                    break
                if (len(jugadasLegales)<p):
                    for q in range(len(jugadasLegales[p])-1):
                        shrC=jugadasLegales[p][-1]
                        if (shrC=='N' or shrC=='A' or shrC=='R' or shrC=='V'):
                            
                            for n, lista in enumerate(listas_de_tablero):
                                listas_de_tablero[n] = lista[::-1]
                                if (SaveN!=n):
                                    contR=0
                                SaveN=n
                                contR=+1
                                condicionrep=1
                                condicion3=1
                                if (contR>3):
                                    if (lista.cadena==shrC and lista.numero1 == jugadasLegales[p][-q]):
                                            tablero.append(lista)
                                            jugadasLegales[p].remove(lista.numero1)
                                            lista.cadena.pop()
                                            lista.numero1.pop()
                                            condicion3=0
                                            print("x")
                                            print("3")
                                            condicionrep=0

                                if (condicion3!=0):
                                    for element2 in (lista_de_fichasBot[turno_actual-1]):
                                        if element2.cadena==shrC and element2.numero1 == jugadasLegales[p][-q]:
                                            tablero.append(element2)
                                            jugadasLegales[p].remove(element2.numero1)
                                            element2.cadena.pop()
                                            element2.numero1.pop()
                                if (condicionrep!=0):
                                    n=0
                if (len(jugadasLegales)<p and len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        break
                            


                lista_de_fichasBotFT=[]
                # ahora se revisa en base a las que comparten el numero y tienen colores diferentes
                if (  checkDeckLen==len(lista_de_fichasBot[turno_actual-1]) and (len(jugadasLegales))>0):
                    for x, lista in enumerate(listas_de_tablero):
                    
                    
                        lista_de_fichasBotP.extend(lista)
                    
                
                        for element1 in (lista_de_fichasBotP):
                            lista_de_fichasBotFT.append(element1)
                            
                    lista_de_fichasBotFT.extend(lista_de_fichasBot[turno_actual-1])
                    jugadasLegales=determinarJugadas(lista_de_fichasBotFT)
                    listaPreferent=0

                    for p in range (0, len(jugadasLegales)-1):
                        if (len(jugadasLegales[p])>len(jugadasLegales[listaPreferent])):
                            listaPreferent=p

                    p=listaPreferent
                    if (len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        print("8")
                        break
                    if (len(jugadasLegales[p])==1):
                        listas_de_tablero.append(tablero)
                        print("7")
                        break
                    contR=0
                    # aqui se revisa primero el mazo, ya que no importa si se quita una ficha central de 
                    #alguna jugada del tablero
                    for q in range(len(jugadasLegales[p])-1):
                        shrC=jugadasLegales[p][-1]
                
                        condicion3=1
                        for element3 in (lista_de_fichasBot[turno_actual-1]):
                            
                        
                            if (element3.numero1==shrC and element3.cadena == jugadasLegales[p][q]):
                                    tablero.append(element3)
                                    jugadasLegales[p].remove(element3.cadena)
                                    element3.cadena.pop()
                                    element3.numero1.pop()
                                    print("X")
                                    print("4")
                                    
                                    condicion3=0
                        contR=0
                        if (condicion3!=0):
                            for n,  lista in enumerate(listas_de_tablero):
                                listas_de_tablero[n] = lista[::-1]
                                contR=0
                                SaveN=n
                                contR=+1
                                # se revisa si la lista tiene mas de 3 elementos
                                if (lista.numero1==shrC and lista.cadena == jugadasLegales[p][q]):
                                    if (len(n>3)):
                                        tablero.append(lista)
                                        jugadasLegales[p].remove(lista.cadena)
                                        lista.cadena.pop()
                                        lista.numero1.pop()
                                        print("X")
                        if (len(jugadasLegales[p])==1):
                            listas_de_tablero.append(tablero)
                            print("6")

                            break
            jugadasLegales=[]
            break
        
    # por si se quiere mostrar que al menos 1 ficha fue bajada
    #if (checkDeckLen>len(lista_de_fichasBot[turno_actual-1])):
        #se habra añadido al menos 1 ficha del bot
    # si se acabaron las fichas del bot, se saca de los turnos
  
    if (len(lista_de_fichasBot[turno_actual-1])==0):
        print(f"Se agotaron las fichas del Bot {turno_actual-1}!")
        turnos.dequeue(turno_actual)
    # si no se bajo ninguna ficha, automaticamente se come
    if (checkDeckLen==len(lista_de_fichasBot[turno_actual-1])):
        FichasJ=sacar_ficha_de_pila(mi_pozo_de_fichas) 
        lista_de_fichasBot[turno_actual-1].append(Ficha(FichasJ.cadena, FichasJ.numero1, FichasJ.numero2))
        
        determinarJugadas
