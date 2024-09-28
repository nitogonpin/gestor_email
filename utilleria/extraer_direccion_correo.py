import pymongo
import email

def recuperarDaseDatosMongoDB(direccion):
    """
    Recupera los correos electrnicos guardados en la base de datos MongoDB
    para la cuenta de correo especificada

    :param direccion: La cuenta de correo de Gmail
    :type direccion: str
    :return: Una lista de direcciones de correo electr nico
    :rtype: list[str]
    """
    # Conecta a la base de datos MongoDB
    # La variable "client" es la conexi n a la base de datos
    client = pymongo.MongoClient("mongodb://localhost:2018")

    # Selecciona la base de datos "correos"
    # La variable "db" es la base de datos seleccionada
    db = client["correos"]

    # Selecciona la colecci n que se indica en la variable "direccion"
    # La variable "collection" es la colecci n seleccionada
    collection = db[direccion]

    # Inicializa una lista vac a para guardar las direcciones de correo
    # La variable "lista_direcciones" es la lista vac a
    lista_direcciones = []

    # Itera sobre los documentos de la colecci n y extrae el campo "from"
    # de cada documento y lo agrega a la lista "lista_direcciones"
    for document in collection.find():
        lista_direcciones.append(document["from"])

    # Cierra la conexi n a la base de datos
    client.close()

    # Devuelve la lista de direcciones de correo electr nico
    return lista_direcciones

def limpiar_direccion(direccion):
    """
    Esta funci n toma una cadena de texto que representa una direcci n
    de correo electr nico y devuelve una cadena con la direcci n limpia
    de etiquetas HTML.

    La direcci n de correo electr nico puede tener etiquetas HTML que
    la envuelven, por ejemplo, "<span>juan.perez@example.com</span>".
    La funci n busca la primera etiqueta "<" y la  ltima etiqueta ">"
    y devuelve la cadena que est  dentro de ambas etiquetas.

    :param direccion: La cadena con la direcci n de correo electr nico
    :type direccion: str
    :return: La direcci n de correo electr nico limpia de etiquetas HTML
    :rtype: str
    """

    # Busca la primera etiqueta "<" en la cadena de texto
    # La variable "start" es el  ndice en el que se encuentra la etiqueta "<"
    start = direccion.find("<") + 1

    # Busca la  ltima etiqueta ">" en la cadena de texto
    # La variable "end" es el  ndice en el que se encuentra la etiqueta ">"
    # El segundo par metro de la funci n find() es el  ndice desde el que se busca
    end = direccion.find(">", start)

    # Devuelve la cadena que est  dentro de ambas etiquetas
    # La variable "direccion_limpia" es la cadena que se devuelve
    return direccion[start:end]


def main():
    # Pide al usuario que introduzca su correo electr nico
    direccion = input("Introduce tu correo: ")

    # Recupera los correos electr nicos de la base de datos MongoDB
    # que se encuentran en la carpeta del usuario
    lista_direcciones = recuperarDaseDatosMongoDB(direccion)

    # Crea un conjunto vac o para almacenar las direcciones de correo
    # electr nico limpias
    lista_direcciones_limpia = set()

    # Itera sobre la lista de direcciones de correo electr nico
    # y las limpia de etiquetas HTML
    for i in lista_direcciones:
        # Limpia la direcci n de correo electr nico
        # de etiquetas HTML
        linea_a_limpiar = limpiar_direccion(i)

        # Agrega la direcci n limpia al conjunto
        lista_direcciones_limpia.add(linea_a_limpiar)

    # Imprime las direcciones de correo electr nico limpias
    for i in lista_direcciones_limpia:
        print(i)

    # Imprime el n mero de correos electr nicos recuperados
    print( "*" * 24)
    print("Recuperados: ", len(lista_direcciones_limpia), " correos.")
    print( "*" * 24)


if __name__ == "__main__":
    main()
