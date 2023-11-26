import csv
import subprocess
from datetime import datetime

hora =datetime.now().time().strftime('%H:%M')
file = str('Tabla-' + datetime.today().strftime('%Y-%m-%d') + '.csv')

with open('Usuarios.csv',newline='') as f:
   reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
   for row in reader:      
    print("{} Usuarios".format(len(row)-1))
peticion=[hora,]
#for i in range(1,len(row)):
for i in range(1,5):
    print("Usuario: {}".format(row[i]))
    #num=int(subprocess.run(["grep", "-c", "INFO -> Integration {}".format(row[i]), "/home/Consultor/Desktop/linux/REMEDY.log"],capture_output=True).stdout)
    num=subprocess.Popen(["grep", "-c", "INFO -> Integration {}".format(row[i]), "/home/Consultor/Desktop/linux/REMEDY.log"],stdout=subprocess.PIPE)
    valor = num.communicate()[0].decode('utf-8')
    peticion.append(str(valor.strip()))

with open("Tabla.csv", 'a', newline='') as csvfile:
   csvwriter=csv.writer(csvfile)
   csvwriter.writerow(peticion)     
   csvfile.close()





