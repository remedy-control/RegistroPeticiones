import argparse
import csv
from datetime import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument('--client', type=str, help='Cliente que ejecuta la peticion')
parser.add_argument('--type', type=str, help='Tipo de peticion que ejecuta el cliente')
args = parser.parse_args()

path='/home/remedy/RegistroPeticiones/'
file = str('Registro-' + datetime.today().strftime('%Y-%m-%d') + '.csv')
tmpFile = 'tmp.csv'

with open(path + file) as fileRead:
    with open(path + tmpFile, 'wb') as fileWrite:
        reader = csv.reader(fileRead, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row[0] == args.client and row[1] == args.type:
                currectCount = row[2]
                newCount = int(row[2]) + 1
                row[2] = row[2].replace(currectCount, str(newCount))
                csv.writer(fileWrite).writerow(row)
            else:
                csv.writer(fileWrite).writerow(row)

os.remove(path + file)
os.rename(path + tmpFile, path + file)