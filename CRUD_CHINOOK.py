#Marcelo Lozada
#04/04/2025
#Archivo para conectar a la base de datos y realizar una consulta

#Importar librerias
import psycopg
def connectar(dbname):
    connexio = f"""
    dbname={dbname}
    user=postgres
    password=postgres
    host=localhost
    port=5432
    """

    conn = psycopg.connect(connexio)
    cur = conn.cursor()
    return cur

#Definicion para mostrar el menu
def printar_menu():
    print("Menú Principal")
    print("1 - Consultar tots els artistes")
    print("2 - Consultar artistes pel seu nom")
    print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
    print("4 - Afegir un artista")
    print("5 - Modificar el nom d'un artista")
    print("6 - Borrar un artista")
    print("7 - Sortir")

#Definicion para consultar artistas
def consultar_artistas():
    resultado = cur.execute("Select * from artist")
    lista = resultado.fetchall()
    print(lista)

#Definicion que consluta artistas por el nombre
def consultar_artistas_nombre():
    while seguir == "n" or seguir == "no":
        consulta = input("Que nombre quieres consultar? ")
        resultado = cur.execute(f"Select * from artist where name={consulta}")
        lista = resultado.fetchall()
        print(lista)
        seguir = input("Quieres consultar otro?(s/n) ").lower()

#Definicion para consultar los 5 primeros albunes
def consultar_5primeros_albunes():
    resultado = cur.execute("Select * from artist limit 5")
    lista = resultado.fetchall()
    print(lista)

#Definicion para añadir artistas
def anadir_artista():
    while seguir == "n" or seguir == "no":
        nombre = input("Como se llama el artista que quieres añadir? ")
        resultado = cur.execute(f"Insert into artista values ((Select Max(artist_id) from artist) +1,'{nombre}')")
        lista = resultado.fetchone()
        print(lista)
        seguir = input("Quieres consultar otro?(s/n) ").lower()

#Definicion para modificar un artista
def modificar_artista():
    while seguir == "n" or seguir == "no":
        nombre = input("Como se llama el artista que quieres modificar? ")
        name_id = input("Quieres modificar el nombre o la id?(name/id) ").lower()
        
        if name_id == "name":
            cambio = input("Dime el nombre que le quieres poner: ")
            resultado = cur.execute(f"Update artist set name = '{cambio}' where name = '{nombre}")
            lista = resultado.fetchone()
            print(lista)
        elif name_id == "id":
            cambio = input("Dime la id que le quieres poner: ")
            resultado = cur.execute(f"Update artist set name = '{cambio}' where name = '{nombre}")
            lista = resultado.fetchone()
            print(lista)
            

        seguir = input("Quieres consultar otro?(s/n) ").lower()

#Definicion para escoger un valor
def opcion_escoger():
    opcion = input("Selecciona una opció: ")
    
    while opcion != "7":
        opcion = input("Selecciona una opció: ")
        if opcion == 1:
            consultar_artistas()
        elif opcion == 2:
            consultar_artistas_nombre()
        elif opcion == 3:
            consultar_5primeros_albunes()
        elif opcion == 4:
            anadir_artista()
        elif opcion == 5:
            modificar_artista()
        elif opcion == 6:
            borrar_artista()
        else:
            print("Selecciona uno de esos 7")

#Main
def main():
    cursor = connectar()
    nomBBDD = input("Introduce el nombre de la base de datos: ")
    connectar(nomBBDD)
    print("Conectado a la base de datos")
    
    printar_menu()


    

if __name__ == "__main__":
    main()
