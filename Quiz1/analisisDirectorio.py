import os
import sys

def analizar_archivos(directorio):
    informe = []
    archivos_txt = [f for f in os.listdir(directorio) if f.endswith('.txt')]
    
    if not archivos_txt:
        informe.append("No se encontraron archivos de texto.")
    else:
        for archivo in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo)
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                    num_lineas = len(lineas)
                    num_palabras = sum(len(linea.split()) for linea in lineas)
                    num_python = sum(linea.lower().count('python') for linea in lineas)
                    
                    informe.append(f"Nombre del archivo: {archivo}")
                    informe.append(f"Número de líneas: {num_lineas}")
                    informe.append(f"Número total de palabras: {num_palabras}")
                    informe.append(f"Número de veces que aparece 'Python': {num_python}")
                    informe.append("")  # Añade una línea en blanco para separación

            except FileNotFoundError:
                informe.append(f"Error: El archivo {archivo} no fue encontrado.")
            except PermissionError:
                informe.append(f"Error: No se tienen permisos para leer el archivo {archivo}.")
            except Exception as e:
                informe.append(f"Error al procesar el archivo {archivo}: {e}")

    return "\n".join(informe)

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]

    if not os.path.isdir(directorio):
        print(f"Error: El directorio {directorio} no existe.")
        sys.exit(1)

    informe = analizar_archivos(directorio)

    with open(os.path.join(directorio, 'informe.txt'), 'w', encoding='utf-8') as f:
        f.write(informe)

if __name__ == "__main__":
    main()