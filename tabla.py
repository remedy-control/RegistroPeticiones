import csv
import subprocess
from datetime import datetime

hora =datetime.now().time().strftime('%H:%M')
file = str('Tabla-' + datetime.today().strftime('%Y-%m-%d') + '.csv')

with open('/home/remedy/TablaPeticiones/Usuarios.csv') as f:
   reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
   for row in reader:      
    print(len(row))
peticion=[hora,]
for i in range(1,len(row)):
    print("Usuario: {}".format(row[i]))
    #num=int(subprocess.call(["grep", "-c", "INFO -> Integration {}".format(row[i]), "/home/remedy/tomcat/logs/REMEDY.log"],capture_output=True).stdout)
    #num=subprocess.Popen(["grep", "-c", "INFO -> Integration {}".format(row[i]), "/home/remedy/tomcat/logs/REMEDY.log"],stdout=subprocess.PIPE)
    num=subprocess.Popen(["grep", "-cw", ":integrationName>{}".format(row[i]), "/tomcat/apache-tomcat-7.0.99/logs/catalina.out"],stdout=subprocess.PIPE)
    valor = num.communicate()[0].decode('utf-8')
    peticion.append(str(valor.strip()))
    
print(file)
with open('/home/remedy/TablaPeticiones/{}'.format(file), 'a') as csvfile:
   csvwriter=csv.writer(csvfile)
   csvwriter.writerow(peticion)     
   csvfile.close()