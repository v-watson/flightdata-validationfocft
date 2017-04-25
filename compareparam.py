## Compare a parameter between two test points from HeliSHOLDS ##
## LEUT V. Watson - 05 Mar 17 MRH-90 FOCFT PH 2 ##
## The following code takes a parameter (defined in the code) ##
## and compares it with another test point (defined by T<EVENT NUMBER>) ##

import zipfile
import pylab as pl
import os

# Take required input files of Torque
t_no = input("Select first 'T' number for analysis: ")
t_no_sec = input("Select second 'T' number for analysis: ")

os.chdir("Evolution T%s" % t_no)

print("Unzipping first test point file...")
# Unzip the target file
zip_ref = zipfile.ZipFile("evol.csv.zip", "r")
zip_ref.extractall()
zip_ref.close()

# Set variables for plot
torque_1 = [0]
torque_2 = [0]
x = 0
y = 0
time = [0]
time_sec = [0]

# Read CSV File
print("Reading first test point file...")
readfile = open('evol.csv', 'r')

# Go through each record in the CSV file for Torque and store
for record in readfile:
    columns = record.split(',')
    
    if columns[1].count('MRH_Torque') == 1:
        if float(columns[2]) > 0:
            torque_1.append(float(columns[2]))
            time.append(x)
            x = x + 1
        else:
            continue
    else:
        continue

print("%s values read" % x)
readfile.close()
print("Closing first test point file...")    
os.remove("evol.csv")

print("Selecting second test point file...")
os.chdir("../Evolution T%s" % t_no_sec)
print("Unzipping second test point file...")
# Unzip the target file
zip_ref = zipfile.ZipFile("evol.csv.zip", "r")
zip_ref.extractall()
zip_ref.close()

# Set variables for plot
torque_2 = [0]

print("Reading second test point file...")
# Read CSV File
readfile = open('evol.csv', 'r')

# Go through each record in the CSV file for Torque and store
for record in readfile:
    columns = record.split(',')
    
    if columns[1].count('MRH_Torque') == 1:
        if float(columns[2]) > 0:
            torque_2.append(float(columns[2]))
            time_sec.append(y)
            y = y + 1
        else:
            continue
    else:
        continue

print("%s values read" % y)
readfile.close()
print("Closing second test point file...")
os.remove("evol.csv")

# Plot Torques vs Time
pl.plot(time, torque_1)
pl.plot(time_sec, torque_2)
pl.show()

input("Press any key to continue. ")