import zipfile
import pylab as pl
import os

# Take required input file of Torque from the 
t_no = input("Select 'T' number for analysis: ")

os.chdir("Evolution T%s" % t_no)

# Unzip the target file
zip_ref = zipfile.ZipFile("evol.csv.zip", "r")
zip_ref.extractall()
zip_ref.close()

# Set variables for plot
torque = [0]
x = 0
time = [0]

# Read CSV File
readfile = open('evol.csv', 'r')

# Go through each record in the CSV file for Torque and store
for record in readfile:
    columns = record.split(',')
    
    if columns[1].count('TORQUE') == 1:
        torque.append(float(columns[2]))
        time.append(x)
        x = x + 1
    else:
        continue

# Plot Torque vs Time
pl.plot(time, torque)
pl.show()

readfile.close()
os.remove("evol.csv")

input("Press any key to continue. ")