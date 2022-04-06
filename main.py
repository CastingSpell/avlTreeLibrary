##########################################################################
# Preparaciones previas                                                  #
##########################################################################

import pandas as pd
import csv
import random

# Importamos las clases Biblioteca y Libro
from dependencias import * 

# Librería para animación mientras se genera el árbol
import threading as th
from time import sleep


##########################################################################
# Definición de las funciones que permitirán la ejecución del programa   #
##########################################################################


def intro():
    '''Muestra mensaje de carga mientras se crean los árboles'''

    print('\n\t')
    for char in '''    Cargando datos y generando árboles
                   Espere por favor...''':
        sleep(0.05)
        print(char, end='', flush=True)

# Creamos e iniciamos un proceso para mostrar el texto de intro() y cargar lo arboles simultaneamente
carga = th.Thread(target = intro)
carga.start()

def accederLib(libro):  # Solo se podrá acceder al libro si lo buscas directamente
    ''' Tras buscar el libro en la biblioteca, se preguntará si desea hacer algo con el
    de ser la respuesta afirmativa, se llamará a esta función, la cual buscará en el libro
    solicitado en la librería y se ofrecerán varias acciones en caso de haber existencias'''

    try:
        if libro.ejemplares() > 0:
            opc = input('Tenemos {} ejemplares del libro seleccionado, desea tomar prestado uno? [y/n]')
            if opc in ['Y', 'y']:
                libro.ejemplares(-1)    # Sacamos un libro de la librería
                print(' * Te has llevado el libro, disfrútalo')
    except:
        print('Solo queda el ejemplar de exposición, lo sentimos\n')

def checkAuth(auth, libro):
    ''' Función que comprobará si el autor ya tiene algún libro registrado en la biblioteca
    de ser ese el caso, en vez de crear una nueva entrada, se actualizará el libro que tenía
    y se convertirá en una lista de libros.'''
    try:
        # Mira si el autor ya está en la biblioteca
        temp = Biblio.ord_autor[auth]
        # print(temp, type(temp))
        if type(temp) is list:
                Biblio.ord_autor[auth].append(libro)
        else:
            Biblio.ord_autor[auth] = [temp, libro]
        # print('Si estaba, lsita creada', Biblio.ord_autor[auth] )
        return True                                        

    except: # De no estarlo, devuelve un falso 
        return False

def checkTitle(libro): 
    ''' Comprueba si el titulo ya está en la biblioteca, teniendo en cuenta que libros con 
    varios autores aparecerán repetidos. Por lo que si y solo sí el libro tiene el mismo 
    titulo y autor, se añadirá a Librería() con de la forma LibroLib() especificando la
    la cantidad, que por defecto será 1.'''
    try:
        # Mira si el libro ya está en la biblioteca
        Biblio.ord_titulo[libro] 
        return True

    except:
        return False

def abastecimiento(file_name, num_repes):
    '''Abastecimiento creará a partir del dataset original (books.csv) un nuevo archivo donde
    se pondrán aleatoriamente una cantidad de libros, también escogidos al azar. Posteriormente
    se fusionarán en el mismo archivo para su posterior gestión de modo de Biblitoeca / Librería'''

    random_list = []

    books2 = open('books2.csv', 'w',  newline='', encoding='utf8')
    books2 = csv.writer(books2)

    for i in range(0, num_repes):
        random_list.append(random.randint(0,10000))

    with open('books.csv', encoding='utf8') as dataset:
        books = csv.reader(dataset)
        next(books, None)   # Para saltar la cabecera
        for fila in books:
            if int(fila[0]) in random_list:
                books2.writerow(fila)
    
    booksF = csv.writer(open(file_name, 'w', newline='', encoding='utf8'))
    books1, books2 = csv.reader(open('books.csv', 'r',  newline='',  encoding='utf8')), csv.reader(open('books2.csv', 'r',  newline='', encoding='utf8'))

    for fila in books1:
        booksF.writerow(fila)
    for fila in books2:
        booksF.writerow(fila)

def menu():
    ''' Maneja el menú y las opciones, función principal para realizar las busquedas'''
    while True:
        opt = input('''








    =======================================================
    |   1. Busqueda por titulo                            |
    |   2. Busqueda por autor                             |
    |   3. Listar todo por orden alfabético (título)      |
    |   4. Listar todo por orden alfabético (autor)       |
    |   5. Salir                                          |
    =======================================================







        Escribe su elección -> ''')

        libro_result = [False, 'obejeto_libro']

        if opt in ('1','2','3','4','5'):       # No convertimos a int directamente el input para evitar errores al escribir letras

            if int(opt) == 1:
                libro = str(input('\n\tLibro a buscar: ')).title()
                try:
                    try: # Intentamos tomar el ejemplar de la libreria
                        print(Libreria.ord_titulo[libro])
                        libro_result = [True, libro]
                    except KeyError: # Si no está en la librería mostramos el de la biblioteca
                        print(Biblio.ord_titulo[libro])
                except KeyError:    # Si no está en ninguna, mostramos los vecinos
                    print('\n{} no se ha encontrado, mostrando el anterior y posterior...\n'.format(libro))
                    print(Biblio.ord_titulo.find_lt(libro)[1])
                    print('Posición en la que iría ',libro)
                    print(Biblio.ord_titulo.find_gt(libro)[1])

            elif int(opt) == 2:
                autor = str(input('\n\tAutor a buscar: ')).title()
                try:
                    if type(Biblio.ord_autor[autor]) is list:
                        for libro in Biblio.ord_autor[autor]:
                            print(libro)
                    else:
                        print(Biblio.ord_autor[autor])
                except KeyError:
                    print('\n{} no se ha encontrado, mostrando el anterior y posterior...\n'.format(autor))
                    print(Biblio.ord_autor.find_lt(libro)[1])
                    print('Posición en la que iría ',libro)
                    print(Biblio.ord_autor.find_gt(libro)[1])

                # Meter autor en una lista para igualar formato, o corregir entrada y nombre del objeto


            elif int(opt) == 3:
                for libro in iter(Biblio.ord_titulo):
                    print(Biblio.ord_titulo[libro])

            elif int(opt) == 4:
                for libro in iter(Biblio.ord_autor):
                    print(Biblio.ord_autor[libro])

            elif int(opt) == 5:
                break

        else:
            print('\n * Opción no válida')

        if libro_result[0]:
            accederLib(libro_result[1])

        cont = input('¿Desea continuar? [y/n] -> ')
        if cont not in ('y', 'Y'):
            break


##########################################################################
# Ejecución del programa                                                 #
##########################################################################

# Creamos el archivo con libros repetidos
abastecimiento('finalbooks.csv', 1000)

# Importamos y tratamos los libros de abastecimiento() a partir
# del dataset books.csv 
# Fuente: https://www.kaggle.com/jealousleopard/goodreadsbooks
data = pd.read_csv('finalbooks.csv', sep=',', error_bad_lines=False)
data = data[data.columns[[5,7,8,9,12]]]   #ISBN, Autores, Año_pub, titulo, valoración

# Lista para cambiar el formato de los años, ya que el csv lo importa con el punto decimal (float)
years_correct = []      

for row in data.itertuples():
    years_correct.append(str(row[3])[:4])

# Borramos la columnas vieja y añadimos la corregida
data.drop('original_publication_year', 1, inplace=True)
data.insert(3, 'pub_year', years_correct)

# Creamos la biblioteca y guardamos los libros en ella
Biblio = Biblioteca()

# Creamos la librería para guardar los libros repetidos
#   Librería utilizará los libros de LibroLib(), clase herdada de Libro() a
#   diferencia de que en este, se puede incluir la cantidad de libros iguales 
#   como atributo, para así llevar el recuento y modificarlos a nuestro antojo
Libreria = Biblioteca()

# Para cada fila del dataframe creamos unas variables temporales y llamamos a la función Libro()
for i in range(len(data)):    
    t_isbn = data['isbn'][i]
    t_title = data['original_title'][i] 
    t_year = data['pub_year'][i]
    t_rating = data['average_rating'][i]
    t_auth = data['authors'][i]


    # El problema viene cuando un libro es una antología, o tiene más de un autor
    # para solucionar eso, crearemos duplicados de libros, uno por cada autor
    # de esta forma nos servirá para la ampliación y a la vez para no perder datos.
    # ya que cada autor devolverá dicho libro entre los suyos.

    if checkTitle(t_title): # Miramos si el libro está ya en la biblioteca, en caso de estar lo guardamos en la librería
        Libreria.ord_titulo[str(data['original_title'][i])] = LibroLib(t_isbn, t_title, t_auth, t_year, t_rating)
        Libreria.ord_autor[str(data['authors'][i])] = LibroLib(t_isbn, t_title, t_auth, t_year, t_rating)
        # print('Repetido: ', LibroLib(t_isbn, t_title, t_auth, t_year, t_rating))

    else:

        if ',' not in data['authors'][i]:      # Si el autor es una tupla, 1 autor
            Biblio.ord_titulo[str(data['original_title'][i])] = Libro(t_isbn, t_title, t_auth, t_year, t_rating)

            autor_registrado = checkAuth(str(data['authors'][i]), Libro(t_isbn, t_title, t_auth, t_year, t_rating))
            
            if not autor_registrado:           # Miramos si el autor ya está registrado en la biblioteca
                Biblio.ord_autor[str(data['authors'][i])] = Libro(t_isbn, t_title, t_auth, t_year, t_rating)

        else:                           # Si no, varios autores
            cnt=0                       # Creamos un contador para los libros con más de un autor ya que si no, 
                                        # no se añadirían varias veces, si no que se reescribirían

            for aut in t_auth.split(','):          # Para cada autor, replicamos el libro añadiendo aut_{numero} para que no se sobreescriban las claves
                Biblio.ord_titulo[str(data['original_title'][i])+' aut_{}'.format(cnt)] = Libro(t_isbn, t_title, aut, t_year, t_rating)
                Biblio.ord_autor[str(aut)] = Libro(t_isbn, t_title, aut, t_year, t_rating)
                cnt+=1


# Una vez todo cargado lanzamos el menu, que llamará a las
# funciones necesarias e iniciará el programa
menu()