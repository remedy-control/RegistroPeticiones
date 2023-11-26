# Este script crea un archivo para que guarde el registro de peticiones
# del proximo dia.
# Ejemplo: Si el día actual es 10 de febrero del 2023 este script creará el archivo Registro-2023-02-11.csv
# Nota: Aun no funciona este script.

path="/home/remedy/RegistroPeticiones/"
origen="Usuarios.csv"
newFile="Tabla-$(date +%Y)-$(date +%m)-$(date +%d).csv"

cp $path$origen $path$newFile 