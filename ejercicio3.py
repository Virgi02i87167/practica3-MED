def main():
    notas = []
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        
        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10. Intente nuevamente.")
            return
        notas.append(nota)
    
    print("Notas obtenidas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    
    nota_media = sum(notas) / len(notas)
    print(f"Nota media: {nota_media}")
    
    nota_maxima = max(notas)
    nota_minima = min(notas)
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota menor: {nota_minima}")

if __name__ == "__main__":
    main()