import cx_Oracle
import csv

try:
  connection=cx_Oracle.connect(
     user='remedy',
     password='R3m3dy_01',
     #Desarrollo
     dsn='10.191.205.235:1522/ARSP81',
     #QA
    #  dsn='10.119.160.61:1521/ARSP81',
     encoding='UTF-8'
  )
  print(connection.version)
  cursor=connection.cursor()
  cursor.execute("SELECT * FROM ARS_CLIENT ORDER BY ARC_ID ASC")
  rows=cursor.fetchall()
  #for row in rows:
  #  print(row)
except Exception as ex:
  print(ex)

listausuarios=['HORA',]
for row in rows:
  listausuarios.append(row[1])

#Para crear la tabla Usuario que es el template
with open('Usuarios.csv', 'w', newline='') as csvfile:
  csvwriter=csv.writer(csvfile)
  csvwriter.writerow(listausuarios)

# with open('Usuarios.csv', 'a', newline='') as csvfile:
#   csvwriter=csv.writer(csvfile)
#   csvwriter.writerows(listahoras)

#Para crear la tabla Tabla que es donde se registrara las peticiones.
with open('Tabla.csv', 'w', newline='') as csvfile:
  csvwriter=csv.writer(csvfile)
  csvwriter.writerow(listausuarios)

# with open('Tabla.csv', 'a', newline='') as csvfile:
#   csvwriter=csv.writer(csvfile)
#   csvwriter.writerows(listahoras)