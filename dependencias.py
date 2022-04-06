# Importamos sys para acceder a las librerías de AVL
import sys

# Añadimos la carpeta al entorno para evitar errores en la importación
sys.path.insert(0, './libraries')

# Importamos AVL
from avl_tree import AVL

class Biblioteca:
    ''' Biblioteca básica dónde se guarda únicamente un ejemplar
    de cada libro'''

    def __init__(self):
        self.ord_titulo = AVL()
        self.ord_autor = AVL()


class Libro:
    ''' Clase genérica para la creación de libros '''
    def __init__(self, isbn, titulo, autor, ano_pub, rating):
        self.isbn = isbn
        self.titulo = titulo
        self.ano_pub = ano_pub
        self.rating = rating
        self.autor = autor

    def __str__(self):
        return '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Libro:                {}
  Autor:                {}
  ISBN :                {}
  Año publicación:      {}
  Valoración:           {} / 5                                   
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(self.titulo, self.autor, self.isbn, self.ano_pub, self.rating)



class LibroLib(Libro):
    ''' Clase heredada de Libro, diseñada para los libros repetidos, 
    cuenta con un atributo nuevo para llevar el sumatorio de los libros
    disponibles. '''
    def __init__(self, isbn, titulo, autor, ano_pub, rating, cant=1):

        # Llamamos al constructor de Libro
        Libro.__init__(self, isbn, titulo, autor, ano_pub, rating)
        
        # Si un libro no está en en formato LibroLib, implica que la cantidad
        # es 1, por lo que se encuentra en la Biblioteca normal, con la clase
        # Libro() original.

        self.cant = cant    # Nuevo atributo

    def __str__(self):
        return '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Libro:                {}
  Autor:                {}
  ISBN :                {}
  Año publicación:      {}
  Valoración:           {} / 5                                  
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Ejemplares disponibles: {}
'''.format(self.titulo, self.autor, self.isbn, self.ano_pub, self.rating, self.cant)

    def ejemplares(self, cant=0):
        '''Muestra los ejemplares disponibles, en caso de meterle un argumento,
        lo resta a la cantidad que había '''
        self.cant -= cant
        return self.cant