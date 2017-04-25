## Display a parameter from HeliSHOLDS ##
## LEUT V. Watson - 05 Mar 17 MRH-90 FOCFT PH 2 ##
## The following code takes an evolution file (evol.csv.zip format) ##
## and displays parameters defined in the code below ##

import zipfile
import pylab as pl
import os

t_no = input("Select 'T' number for analysis: ")
os.chdir("Evolution T%s" % t_no)

print("Unzipping file...")
# Unzip the target file
zip_ref = zipfile.ZipFile("evol.csv.zip", "r")
zip_ref.extractall()
zip_ref.close()

print("File successfully unzipped.")
# Set variables for plot
torque = [0]
lateral = [0]
longitudinal = [0]
radalt = [0]
x = 0
y = 0
z = 0
m = 0
time_tq = [0]
time_long = [0]
time_lat = [0]
time_radalt = [0]

# Read CSV File
print("Reading CSV...")
readfile = open('evol.csv', 'r')

# Go through each record in the CSV file for Torque Required Parameters
for record in readfile:
    columns = record.split(',')
    
    if columns[1].count('MRH_Torque') == 1:
        torque.append(float(columns[2]))
        time_tq.append(x)
        x = x + 1
    elif columns[1].count('MRH_Longitudinal') == 1:
          longitudinal.append(float(columns[2]))
          time_long.append(y)
          y = y + 1
    elif columns[1].count('MRH_Lateral') == 1:
          lateral.append(float(columns[2]))
          time_lat.append(z)
          z = z + 1            
    elif columns[1].count('MRH_RAD_ALT') == 1:
          radalt.append(float(columns[2]))
          time_radalt.append(m)
          m = m + 1            
    else:
        continue

# Plot Parameters
pl.subplot(411)
pl.plot(time_tq, torque)
pl.grid()
pl.ylabel('Torque (%)')

pl.subplot(412)
pl.plot(time_long, longitudinal)
pl.grid()
pl.ylabel('Longitudinal (%)')

pl.subplot(413)
pl.plot(time_lat, lateral)
pl.grid()
pl.ylabel('Lateral (%)')
pl.xlabel('Time (s)')

pl.subplot(414)
pl.plot(time_radalt, radalt)
pl.grid()
pl.ylabel('RADALT (ft)')
pl.xlabel('Time (s)')

pl.show()

readfile.close()
os.remove("evol.csv")

input("Press any key to continue. ")