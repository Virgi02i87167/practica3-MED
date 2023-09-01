def main():
    cadena = input("Ingrese una cadena: ")
    lista_palabras = cadena.split()
    cantidad_palabras = len(lista_palabras)
    print(f"La cadena tiene {cantidad_palabras} palabra(s).")
    
if __name__ == "__main__":
    main()