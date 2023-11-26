##Con libreria OS 
import os

num=os.system('grep -c \'Integration {}\' REMEDY.log'.format(row[i]))
#################################
#Codigo de Grep
# regexp = re.compile(sys.argv[1])
# print(sys.argv[1])
# i=0
# for arg in sys.argv[2:]:
#     for fn in glob.iglob(arg):
#         with open(fn, encoding="utf8") as file:
#             for line in file:
#                 if re.search(regexp, line):
#                     i+=1
#                     #print(line, end='')
# print(i)


########################################
# num=int(subprocess.run(["grep", "-c", "Integration {}".format(row[0]), "/home/consultor/Desktop/linux/REMEDY.log"],capture_output=True).stdout)
