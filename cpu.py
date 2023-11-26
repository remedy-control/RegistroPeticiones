import subprocess
import csv


num=int(subprocess.run(["top", "-c"],capture_output=True).stdout)

print(num)