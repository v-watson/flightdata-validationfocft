# *************** Extract Desired Parameter from HeliSHOLDS and Display **********
# **** LEUT V. Watson ***
# **** 07 Mar 17 ********

import zipfile
import pylab as pl
import os

print("1 - Torque ")
print("2 - Longitudinal Cyclic")
print("3 - Lateral Cyclic")
print("4 - RADALT")
param = input("Select required parameter: ")

if param == '1':
    param = 'MRH_Torque'
elif param == '2':
    param = 'MRH_Longitudinal'
elif param == '3':
    param = 'MRH_Lateral'
elif param == '4':
    param = 'MRH_RAD_ALT'
else:
    print("Please try again. Selection not recognised")    

t_no = input("Select 'T' number for analysis: ")
os.chdir("Evolution T%s" % t_no)

# Unzip the target file
zip_ref = zipfile.ZipFile("evol.csv.zip", "r")
zip_ref.extractall()
zip_ref.close()

print("File successfully unzipped.")

# Set variables for plot
param_array = [0]
x = 0
time = [0]

# Read CSV File
print("Reading CSV...")
readfile = open('evol.csv', 'r')
os.chdir("../")
filename = "extracted_%s.csv" % param
writefile = open(filename, 'w')

# Go through each record in the CSV file for Torque Required Parameters
for record in readfile:
    columns = record.split(',')
    
    if columns[1].count(param) == 1:
        param_array.append(float(columns[2]))
        time.append(x)
        writestring = "%d,%s\n" % (x, columns[2]) 
        writefile.write(writestring)
        x = x + 1
    else:
        continue
    
pl.plot(time, param_array)
pl.grid()
pl.show()

os.chdir("Evolution T%s" % t_no)
readfile.close()
os.remove("evol.csv")
writefile.close()

input("Press any key to continue. ")
