import copy
import random
from collections import deque
import os
def limpiar_pantalla():
        os.system('clear')
class Pieza:
    def __init__(self, numero, color):
        self.numero = numero
        self.color = color
        self.es_comodin = False
        
    def __str__(self):
        return f"{self.numero}{self.color}" if not self.es_comodin else "COMODIN"

class Jugador:
    def __init__(self, nombre):
        self.fichas = []
        self.nombre = nombre
        self.bajo = False
    def ordenar_fichas(self):
        if self.nombre.endswith("[PC]"):
            bubble_sort(self.fichas)
        else:
            insertion_sort(self.fichas)

        
def crear_piezas():
    colores = ['A', 'V', 'R', 'N']
    piezas = []
    # Crear piezas normales
    for numero in range(1, 14):  # Números del 1 al 13
        for color in colores:  # Colores: 'A', 'V', 'R', 'N'
            for _ in range(2):  # Dos copias de cada pieza
                nueva_pieza = Pieza(numero, color)
                piezas.append(nueva_pieza)
    # Crear comodines
    comodines = []
    for _ in range(2):  # Dos comodines
        comodin = Pieza(0, '')
        comodin.es_comodin = True  # Marcar como comodín
        comodines.append(comodin)
    # Añadir comodines a la lista de piezas
    piezas.extend(comodines)
    # Mezclar todas las piezas
    random.shuffle(piezas)
    return piezas

def insertion_sort(fichas):
    for i in range(1, len(fichas)):
        key = fichas[i]
        j = i - 1
        while j >= 0 and (fichas[j].numero > key.numero or (fichas[j].numero == key.numero and fichas[j].color > key.color)):
            fichas[j + 1] = fichas[j]
            j -= 1
        fichas[j + 1] = key
    
def bubble_sort(fichas):
    n = len(fichas)
    for i in range(n):
        for j in range(0, n-i-1):
            if (fichas[j].numero > fichas[j+1].numero) or (fichas[j].numero == fichas[j+1].numero and fichas[j].color > fichas[j+1].color):
                fichas[j], fichas[j+1] = fichas[j+1], fichas[j]


   
    
    
def buscar_grupos(fichas):
    grupos = []
    fichas_por_numero = {}
    
    # Agrupar fichas por número, ignorando los comodines inicialmente.
    for ficha in fichas:
        if not ficha.es_comodin:
            if ficha.numero not in fichas_por_numero:
                fichas_por_numero[ficha.numero] = []
            fichas_por_numero[ficha.numero].append(ficha)

    # Añadir comodines a la consideración.
    comodines = [ficha for ficha in fichas if ficha.es_comodin]
    num_comodines = len(comodines)

    # Formar grupos válidos, asegurando que los colores no se repitan.
    for numero, fichas_agrupadas in fichas_por_numero.items():
        if len(fichas_agrupadas) + num_comodines >= 3:
            colores_vistos = set()
            grupo = []
            
            for ficha in fichas_agrupadas:
                if ficha.color not in colores_vistos:
                    grupo.append(ficha)
                    colores_vistos.add(ficha.color)
            
            # Utilizar comodines si es necesario para llegar a un mínimo de 3 fichas.
            while len(grupo) + len(comodines) >= 3 and len(grupo) < 3:
                grupo.append(comodines.pop(0))
            
            # Solo añadir el grupo si es válido.
            if len(grupo) >= 3:
                grupos.append(grupo)

    return grupos
def es_jugada_valida(jugada):
    if len(jugada) < 3:
        return False
    
    # Validar grupos
    if all(ficha.numero == jugada[0].numero for ficha in jugada):
        colores = set(ficha.color for ficha in jugada if not ficha.es_comodin)
        return len(colores) == len([ficha for ficha in jugada if not ficha.es_comodin])
    # Validar secuencias
    elif all(ficha.color == jugada[0].color for ficha in jugada):
        numeros = sorted(ficha.numero for ficha in jugada if not ficha.es_comodin)
        return all(numeros[i] + 1 == numeros[i + 1] for i in range(len(numeros) - 1))
    
    return False
def buscar_secuencias(fichas):
    secuencias = []
    fichas_por_color = {}
    for ficha in fichas:
        if not ficha.es_comodin:
            if ficha.color not in fichas_por_color:
                fichas_por_color[ficha.color] = []
            fichas_por_color[ficha.color].append(ficha)

    comodines = [ficha for ficha in fichas if ficha.es_comodin]
    num_comodines = len(comodines)

    for color, fichas_agrupadas in fichas_por_color.items():
        fichas_agrupadas.sort(key=lambda x: x.numero)
        secuencia_actual = []
        ultimo_numero = None

        for ficha in fichas_agrupadas:
            if ultimo_numero is None or ficha.numero == ultimo_numero + 1:
                secuencia_actual.append(ficha)
                ultimo_numero = ficha.numero
            else:
                gap = ficha.numero - ultimo_numero - 1
                if num_comodines >= gap and gap > 0:
                    secuencia_actual.extend(comodines[:gap])
                    secuencia_actual.append(ficha)
                    num_comodines -= gap
                    ultimo_numero = ficha.numero
                else:
                    if len(secuencia_actual) >= 3:
                        secuencias.append(secuencia_actual)
                    secuencia_actual = [ficha]
                    ultimo_numero = ficha.numero

        if len(secuencia_actual) >= 3:
            secuencias.append(secuencia_actual)

    return secuencias



def bajar_piezas(jugador, pozo, mesa):
    opciones = buscar_grupos(jugador.fichas) + buscar_secuencias(jugador.fichas)
    opciones_validas = [opc for opc in opciones if es_jugada_valida(opc)]

    if not opciones_validas:
        print("No tienes conjuntos válidos para bajar, tomando una pieza del pozo automáticamente...")
        if pozo:
            jugador.fichas.append(pozo.pop())
            print("Pieza tomada del pozo.")
        else:
            print("No hay más piezas en el pozo.")
        return  # Regresa después de tomar la pieza

    print("Opciones para bajar:")
    for idx, opcion in enumerate(opciones_validas, 1):
        print(f"{idx}. {' '.join(str(ficha) for ficha in opcion)}")

    try:
        eleccion = int(input("Selecciona el conjunto que quieres bajar (0 para cancelar): "))
        if eleccion == 0:
            return
        conjunto_bajado = opciones_validas[eleccion - 1]
        for ficha in conjunto_bajado:
            jugador.fichas.remove(ficha)
        jugador.bajo = True
        mesa.append(conjunto_bajado)
        print("Has bajado el siguiente conjunto:")
        print(' '.join(str(ficha) for ficha in conjunto_bajado))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    except IndexError:
        print("Opción inválida.")
        
        
        
def calcular_puntaje(jugada):
    return sum(ficha.numero for ficha in jugada)
def primer_turno(jugador, pozo):
    print(f"Primer turno de {jugador.nombre}")

    # Buscar todas las jugadas posibles
    grupos_posibles = buscar_grupos(jugador.fichas)
    secuencias_posibles = buscar_secuencias(jugador.fichas)
    todas_las_jugadas = grupos_posibles + secuencias_posibles

    # Filtrar las jugadas que sumen más de 31 puntos
    jugadas_validas = [jugada for jugada in todas_las_jugadas if calcular_puntaje(jugada) > 31]

    # Mostrar jugadas válidas, si las hay
    if jugadas_validas:
        print("Puedes empezar a jugar. Aquí están las jugadas que puedes bajar:")
        for idx, jugada in enumerate(jugadas_validas, 1):
            print(f"{idx}. {' '.join(str(ficha) for ficha in jugada)} ({calcular_puntaje(jugada)} puntos)")
    else:
        print("No tienes jugadas que sumen más de 31 puntos. Debes tomar una pieza del pozo.")
        while not jugadas_validas and pozo:
            jugador.fichas.append(pozo.pop())
            grupos_posibles = buscar_grupos(jugador.fichas)
            secuencias_posibles = buscar_secuencias(jugador.fichas)
            todas_las_jugadas = grupos_posibles + secuencias_posibles
            jugadas_validas = [jugada for jugada in todas_las_jugadas if calcular_puntaje(jugada) > 31]
            if jugadas_validas:
                print("Ahora puedes bajar las siguientes jugadas:")
                for idx, jugada in enumerate(jugadas_validas, 1):
                    print(f"{idx}. {' '.join(str(ficha) for ficha in jugada)} ({calcular_puntaje(jugada)} puntos)")
            else:
                print("Todavía no tienes jugadas válidas. Continúas tomando del pozo...")    
                
                
                
    
def agregar_ficha(jugador, mesa, posibles_agregados):
    print("Opciones disponibles para agregar:")
    for idx, (ficha, jugada_idx) in enumerate(posibles_agregados, 1):
        print(f"{idx}. Agregar {ficha} a la jugada {jugada_idx + 1} en la mesa")

    while True:
        try:
            eleccion = input("Seleccione la opción para agregar: ")
            eleccion = int(eleccion) - 1  # Convertimos a int y ajustamos para índice 0-based
            if 0 <= eleccion < len(posibles_agregados):
                break  # Salir del bucle si la elección es válida
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(posibles_agregados)}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    ficha, jugada_idx = posibles_agregados[eleccion]

    # Realizar la acción de agregar
    jugador.fichas.remove(ficha)
    mesa[jugada_idx].append(ficha)
    print(f"Has agregado {ficha} a la jugada {jugada_idx + 1} en la mesa.")
def opciones_de_agregar_ficha(jugador, mesa):
    posibles_agregados = []

    # Explorar cada jugada en la mesa para identificar oportunidades de extensión.
    for idx, jugada in enumerate(mesa):
        # Detección de secuencias
        if all(ficha.color == jugada[0].color for ficha in jugada):
            numeros_jugada = sorted([ficha.numero for ficha in jugada])
            color = jugada[0].color
            min_num = numeros_jugada[0]
            max_num = numeros_jugada[-1]

            # Buscar fichas que se puedan agregar al inicio o al final de la secuencia.
            ficha_inicial = next((ficha for ficha in jugador.fichas if ficha.numero == min_num - 1 and ficha.color == color), None)
            ficha_final = next((ficha for ficha in jugador.fichas if ficha.numero == max_num + 1 and ficha.color == color), None)
            if ficha_inicial:
                posibles_agregados.append((ficha_inicial, idx))
            if ficha_final:
                posibles_agregados.append((ficha_final, idx))

        # Detección de grupos
        else:
            numeros_jugada = {ficha.numero for ficha in jugada}
            numero = jugada[0].numero
            colores_jugada = {ficha.color for ficha in jugada}

            # Buscar fichas que tengan el mismo número pero un color diferente de los ya presentes en el grupo.
            for ficha in jugador.fichas:
                if ficha.numero == numero and ficha.color not in colores_jugada:
                    posibles_agregados.append((ficha, idx))

    return posibles_agregados


def modificar_jugada(jugador, mesa):
    pares_en_mano = encontrar_y_mostrar_pares_en_mano(jugador)
    if not pares_en_mano:
        print("No tienes pares en tu mano para formar nuevas jugadas.")
        return

    print("Selecciona la jugada de la que deseas extraer una ficha (solo se muestran índices):")
    for idx, jugada in enumerate(mesa, 1):
        print(f"{idx}. (Jugada con {len(jugada)} fichas)")

    eleccion_jugada = int(input("Número de jugada: ")) - 1
    jugada_seleccionada = mesa[eleccion_jugada]

    print("Fichas en la jugada seleccionada:")
    for index, ficha in enumerate(jugada_seleccionada, 1):
        print(f"{index}. {ficha}")

    index_ficha = int(input("Elige la ficha que quieres extraer: ")) - 1
    ficha_extraida = jugada_seleccionada.pop(index_ficha)

    # Verificar si la jugada original sigue siendo válida después de extraer la ficha
    if not es_jugada_valida(jugada_seleccionada):
        print("La jugada original no es válida sin esta ficha. Devolviendo la ficha.")
        jugada_seleccionada.insert(index_ficha, ficha_extraida)  # Devolver la ficha a su posición original
        return

    # Continuar con la combinación de la ficha extraída con un par de la mano
    print("Elige el par con el que deseas combinar la ficha extraída:")
    for idx, (idx1, idx2) in enumerate(pares_en_mano, 1):
        print(f"{idx}. {jugador.fichas[idx1]} {jugador.fichas[idx2]}")

    eleccion_par = int(input("Número del par: ")) - 1
    indices_par = pares_en_mano[eleccion_par]
    par_seleccionado = [jugador.fichas[indices_par[0]], jugador.fichas[indices_par[1]]]

    # Formar la nueva jugada y validarla
    nueva_jugada = par_seleccionado + [ficha_extraida]
    if es_jugada_valida(nueva_jugada):
        mesa.append(nueva_jugada)
        print("Nueva jugada válida creada y añadida a la mesa.")
        # Eliminar las fichas del par utilizado de la mano del jugador
        jugador.fichas = [ficha for idx, ficha in enumerate(jugador.fichas) if idx not in indices_par]
    else:
        print("La combinación no forma una jugada válida. Devolviendo las fichas.")
        jugador.fichas.extend(nueva_jugada)  # Devolver todas las fichas a la mano del jugador
        jugada_seleccionada.insert(index_ficha, ficha_extraida)  # Devolver la ficha a la jugada original si la nueva jugada no es válida
def obtener_ficha_de_mano(jugador):
    print("Tus fichas disponibles son:")
    for idx, ficha in enumerate(jugador.fichas, 1):
        print(f"{idx}. {ficha}")

    while True:
        eleccion = input("Elige la ficha que deseas agregar (número): ")
        try:
            eleccion = int(eleccion) - 1  # Ajustar para índice base 0
            if 0 <= eleccion < len(jugador.fichas):
                return jugador.fichas.pop(eleccion)  # Devuelve la ficha y la quita de la mano
            else:
                print(f"Por favor, ingresa un número entre 1 y {len(jugador.fichas)}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
def es_jugada_valida(jugada):
    if len(jugada) < 3:
        return False

    # Separar comodines de fichas normales
    comodines = [ficha for ficha in jugada if ficha.es_comodin]
    fichas_normales = [ficha for ficha in jugada if not ficha.es_comodin]

    if all(ficha.color == fichas_normales[0].color for ficha in fichas_normales):
        # Ordenar las fichas normales por número y tratar de usar comodines para llenar huecos
        numeros = sorted(ficha.numero for ficha in fichas_normales)
        # Contar los comodines necesarios para llenar huecos en una secuencia
        huecos = sum((numeros[i + 1] - numeros[i] - 1) for i in range(len(numeros) - 1))
        if huecos <= len(comodines):
            return True

    elif all(ficha.numero == fichas_normales[0].numero for ficha in fichas_normales):
        # Verificar que los colores sean únicos y usar comodines como colores adicionales si es necesario
        colores = set(ficha.color for ficha in fichas_normales)
        if len(colores) + len(comodines) == len(jugada):
            return True

    return False
def encontrar_y_mostrar_pares_en_mano(jugador):
    pares = []
    fichas_por_numero = {}
    for idx, ficha in enumerate(jugador.fichas):
        if ficha.numero not in fichas_por_numero:
            fichas_por_numero[ficha.numero] = []
        fichas_por_numero[ficha.numero].append(idx)  # Guardar índices, no fichas
    
    # Encontrar pares por número usando índices
    for fichas in fichas_por_numero.values():
        if len(fichas) == 2:
            pares.append((fichas[0], fichas[1]))
    
    # Mostrar los pares encontrados
    if pares:
        print("Pares en tu mano:")
        for idx, (idx1, idx2) in enumerate(pares, 1):
            print(f"{idx}. {jugador.fichas[idx1]} {jugador.fichas[idx2]}")
    else:
        print("No tienes pares en tu mano.")
    
    return pares



def turno_jugador(jugador, pozo, mesa):
    print(f"Turno de {jugador.nombre}")
    grupos_posibles = buscar_grupos(jugador.fichas)
    secuencias_posibles = buscar_secuencias(jugador.fichas)
    juegos_posibles = grupos_posibles + secuencias_posibles
    
    posibles_agregados = opciones_de_agregar_ficha(jugador, mesa)

    opciones_disponibles = [1]

    if juegos_posibles:
        opciones_disponibles.append(2)
    else:
        print("No tienes combinaciones válidas para bajar en este momento.")

    if posibles_agregados:
        print("Tienes la opción de intercambiar fichas con la mesa.")
        opciones_disponibles.append(3)
    if mesa:
        opciones_disponibles.append(4) 

    print("Opciones:")
    if 1 in opciones_disponibles:
        print("1. Agarrar piezas del pozo")
    if 2 in opciones_disponibles:
        print("2. Bajar piezas")
    if 3 in opciones_disponibles:
        print("3. Agregar ficha a la mesa")
    if 4 in opciones_disponibles:
        print("4. Modificar jugada existente")

    eleccion = obtener_opcion_valida(min(opciones_disponibles), max(opciones_disponibles))
    
    if eleccion == 1:
        if pozo:
            jugador.fichas.append(pozo.pop())
            print("Has tomado una pieza del pozo.")
        else:
            if mesa:
                reutilizar_fichas_mesa(pozo, mesa)
                jugador.fichas.append(pozo.pop())
                print("Has tomado una pieza del pozo reciclado.")
            else:
                print("No hay más piezas en el pozo ni en la mesa.")
                
    elif eleccion == 2 and 2 in opciones_disponibles:
        bajar_piezas(jugador, pozo, mesa)
    elif eleccion == 3 and 3 in opciones_disponibles:
        agregar_ficha(jugador, mesa, posibles_agregados)
    elif eleccion == 4:
        modificar_jugada(jugador, mesa)
    else:
        print("Opción inválida")
def obtener_opcion_valida(minimo, maximo):
    """Solicita al usuario una opción válida y verifica que esté dentro del rango permitido."""
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Por favor, ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    


def evaluar_jugada(jugada, fichas):
    # Puntúa la jugada basándose en la cantidad de fichas que usa y las opciones que deja.
    puntaje = sum(ficha.numero for ficha in jugada)
    fichas_restantes = [ficha for ficha in fichas if ficha not in jugada]
    # Añadir puntos extra por dejar opciones abiertas o mantener comodines
    comodines_restantes = sum(1 for ficha in fichas_restantes if ficha.es_comodin)
    puntaje += 5 * comodines_restantes  # Dar prioridad a mantener comodines
    return puntaje
def turno_bot(bot, pozo, mesa, estrategia):
    print(f"Turno de {bot.nombre}")
    if estrategia == 'lazy':
        estrategia_lazy(bot, mesa, pozo)
    elif estrategia == 'greedy':
        estrategia_greedy(bot, mesa, pozo)
    elif estrategia == 'aleatoria':
        estrategia_aleatoria(bot, mesa, pozo)
    print("\n")
def obtener_opciones_modificacion(bot, mesa):
    pares_en_mano = encontrar_y_mostrar_pares_en_mano(bot)
    posibles_modificaciones = []
    for idx, jugada in enumerate(mesa):
        if len(jugada) > 3:
            for i, ficha in enumerate(jugada):
                posibles_modificaciones.append((idx, i, ficha))
    return posibles_modificaciones
def modificar_jugada_bot(bot, mesa, posibles_modificaciones):
    if posibles_modificaciones:
        jugada_idx, ficha_idx, ficha_extraida = posibles_modificaciones[0]
        jugada_seleccionada = mesa[jugada_idx]
        jugada_seleccionada.pop(ficha_idx)
        if es_jugada_valida(jugada_seleccionada):
            mesa[jugada_idx] = jugada_seleccionada
            print(f"{bot.nombre} ha modificado una jugada.")
        else:
            jugada_seleccionada.insert(ficha_idx, ficha_extraida)
def estrategia_lazy(bot, mesa, pozo):
    opciones = buscar_grupos(bot.fichas) + buscar_secuencias(bot.fichas)
    posibles_agregados = opciones_de_agregar_ficha(bot, mesa)
    
    if opciones:
        mejor_opcion = max(opciones, key=lambda jugada: len(jugada))
        for ficha in mejor_opcion:
            bot.fichas.remove(ficha)
        mesa.append(mejor_opcion)
        print(f"{bot.nombre} ha bajado: {' '.join(str(ficha) for ficha in mejor_opcion)}")
    elif posibles_agregados:
        ficha, jugada_idx = posibles_agregados[0]
        bot.fichas.remove(ficha)
        mesa[jugada_idx].append(ficha)
        print(f"{bot.nombre} ha agregado {ficha} a la jugada {jugada_idx + 1} en la mesa.")
    elif pozo:
        pieza_tomada = pozo.pop()
        bot.fichas.append(pieza_tomada)
        print(f"{bot.nombre} ha tomado una pieza del pozo.")
    else:
        print(f"{bot.nombre} no puede jugar y el pozo está vacío.")
def estrategia_greedy(bot, mesa, pozo):
    opciones = buscar_grupos(bot.fichas) + buscar_secuencias(bot.fichas)
    posibles_agregados = opciones_de_agregar_ficha(bot, mesa)
    
    while opciones:
        mejor_opcion = max(opciones, key=lambda jugada: evaluar_jugada(jugada, bot.fichas))
        for ficha in mejor_opcion:
            bot.fichas.remove(ficha)
        mesa.append(mejor_opcion)
        opciones = buscar_grupos(bot.fichas) + buscar_secuencias(bot.fichas)
    if posibles_agregados:
        for ficha, jugada_idx in posibles_agregados:
            bot.fichas.remove(ficha)
            mesa[jugada_idx].append(ficha)
            print(f"{bot.nombre} ha agregado {ficha} a la jugada {jugada_idx + 1} en la mesa.")
    elif pozo:
        pieza_tomada = pozo.pop()
        bot.fichas.append(pieza_tomada)
        print(f"{bot.nombre} ha tomado una pieza del pozo.")
    else:
        print(f"{bot.nombre} no puede jugar y el pozo está vacío.")
def estrategia_aleatoria(bot, mesa, pozo):
    accion = random.choice(['bajar', 'agregar', 'tomar'])
    
    if accion == 'bajar':
        opciones = buscar_grupos(bot.fichas) + buscar_secuencias(bot.fichas)
        if opciones:
            jugada_elegida = random.choice(opciones)
            for ficha in jugada_elegida:
                bot.fichas.remove(ficha)
            mesa.append(jugada_elegida)
            print(f"{bot.nombre} ha bajado: {' '.join(str(ficha) for ficha in jugada_elegida)}")
        elif pozo:
            pieza_tomada = pozo.pop()
            bot.fichas.append(pieza_tomada)
            print(f"{bot.nombre} ha tomado una pieza del pozo.")
        else:
            print(f"{bot.nombre} no puede jugar y el pozo está vacío.")
    
    elif accion == 'agregar':
        posibles_agregados = opciones_de_agregar_ficha(bot, mesa)
        if posibles_agregados:
            ficha, jugada_idx = random.choice(posibles_agregados)
            bot.fichas.remove(ficha)
            mesa[jugada_idx].append(ficha)
            print(f"{bot.nombre} ha agregado {ficha} a la jugada {jugada_idx + 1} en la mesa.")
        elif pozo:
            pieza_tomada = pozo.pop()
            bot.fichas.append(pieza_tomada)
            print(f"{bot.nombre} ha tomado una pieza del pozo.")
        else:
            print(f"{bot.nombre} no puede jugar y el pozo está vacío.")
    
    else:
        if pozo:
            pieza_tomada = pozo.pop()
            bot.fichas.append(pieza_tomada)
            print(f"{bot.nombre} ha tomado una pieza del pozo.")
        else:
            print(f"{bot.nombre} no puede jugar y el pozo está vacío.")



def verificar_jugadas_mesa(mesa):
    for jugada in mesa:
        if not es_jugada_valida(jugada):
            print("Se ha detectado una jugada inválida en la mesa.")
            return False
    return True
def comprobar_ganador(jugadores):
    for jugador in jugadores:
        if not jugador.fichas:  # Lista de fichas del jugador está vacía
            return jugador
    return None
def simular_turnos(jugadores, pozo, mesa):
    turno_deque = deque(jugadores)
    primer_turno_realizado = {jugador: False for jugador in jugadores}

    while pozo and any(jugador.fichas for jugador in jugadores):
        jugador_actual = turno_deque[0]
    
        if not primer_turno_realizado[jugador_actual]:
            primer_turno(jugador_actual, pozo)
            primer_turno_realizado[jugador_actual] = True
        else:
            if jugador_actual.nombre.endswith("[PC]"):
                estrategia = random.choice(['lazy', 'greedy', 'aleatoria'])
                turno_bot(jugador_actual, pozo, mesa, estrategia)
            else:
                turno_jugador(jugador_actual, pozo, mesa)

        ganador = comprobar_ganador(jugadores)
        if ganador:
            print(f"¡Felicidades {ganador.nombre}! Has ganado el juego.")
            return

        imprimir_estado_juego(jugadores, pozo, mesa)
        turno_deque.rotate(-1)
        input("Presiona Enter para continuar al siguiente turno...")
def reutilizar_fichas_mesa(pozo, mesa):
    if len(mesa) > 1:
        # Extraer todas las fichas excepto las de la última jugada agregada
        fichas_para_reutilizar = [ficha for jugada in mesa[:-1] for ficha in jugada]
        pozo.extend(fichas_para_reutilizar)
        random.shuffle(pozo)
        # Vaciar las jugadas utilizadas, excepto la última
        del mesa[:-1]
        print("Se han reutilizado las fichas de la mesa.")
    elif len(mesa) == 1 and len(pozo) == 0:
        # Si solo hay una jugada en la mesa y el pozo está vacío, se reutiliza esa jugada también
        pozo.extend(mesa[0])
        random.shuffle(pozo)
        mesa.clear()
        print("Se han reutilizado todas las fichas de la mesa.")

        
       
def imprimir_estado_juego(jugadores, pozo, mesa):
    print("-----Rummy Status-----")
    for idx, jugador in enumerate(jugadores, 1):
        jugador.ordenar_fichas()
        fichas_jugador = ' '.join(str(ficha) for ficha in jugador.fichas)
        print(f"{jugador.nombre}")
        print(f"Fichas: {fichas_jugador}")
    print(f"POZO: {len(pozo)} fichas restantes")
    print("MESA:")
    for idx, jugada in enumerate(mesa, 1):
        jugada_str = ' '.join(str(ficha) for ficha in jugada)
        print(f"(Jugada {idx}): {jugada_str}")


def main():
    nombre_jugador = "Angel"
    piezas = crear_piezas()
    jugadores = [Jugador(nombre_jugador), Jugador("Bot[PC]")]


    for jugador in jugadores:
        jugador.fichas = [piezas.pop() for _ in range(14)]

    pozo = piezas
    mesa = []

    imprimir_estado_juego(jugadores, pozo, mesa)
    simular_turnos(jugadores, pozo, mesa)
if __name__ == "__main__":
    main()