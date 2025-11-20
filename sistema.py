import csv
import os

class CRUD:

    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "edad"])

    def obtener_nuevo_id(self, archivo):
        with open(archivo, "r") as f:
            filas = list(csv.reader(f))

        if len(filas) == 1:
            return 1

        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1

    def crear(self, archivo, nombre, edad):
        id_nuevo = self.obtener_nuevo_id(archivo)
        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id_nuevo, nombre, edad])
        return id_nuevo

    def listar(self, archivo):
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)
        
    def eliminar(self,archivo,id_eliminar):
        with open(archivo, "r")as f :
            reader= csv.reader(f)
            filas=list(reader)
        filas_filtradas=[filas[0]]
        encontrado=False
        for fila in filas[1:]:
            if fila[0]!=str(id_eliminar):
                filas_filtradas.append(fila)
            else:
                encontrado=True
        if encontrado :
            with open(archivo, "w" , newline=("")) as f:
                writer= csv.writer(f)
                writer.writerow(filas_filtradas)
            print(f"persona con id {id_eliminar} eliminado")
        else:
            print(f"no se encontro el id {id_eliminar}")

    def actualizar(self,archivo,id_actualizar,nuevo_nombre,nuevo_edad):
        with open (archivo,"r" )as f:
           reader=csv.reader(f)
           filas=list(reader)
           filas_actualizar=[filas[0]]
           encontrado=False
        for fila in filas[1:]:
          if fila[0] == str(id_actualizar):
              filas_actualizar.append([fila[0],nuevo_nombre,nuevo_edad])
              encontrado=True
        else:
            filas_actualizar.append(fila)
            if encontrado:
                with open(archivo,"w", newline="") as f:
                    writer= csv.writer(f)
                    writer.writerow(filas_actualizar)
                print(f"persona con id {id_actualizar} encontrado")
            else:
                print(f"no se encontro {id_actualizar}")


