"""
Title: Anemometer Comparison Script
Date: 23 Aug 16
Author: Viruben
"""

import pylab as pl

# CSV sorted initially using Excel
# FWD Port -Ship's An 2
# Aft Stbd - Ship's An 3

# Set variables for plot
mf2_anem_dir = [0]
mf2_anem_spd = [0]
ship_anem_ws_2_dir = [0]
ship_anem_ws_2_spd = [0]
ship_anem_ws_3_dir = [0]
ship_anem_ws_3_spd = [0]
x_axis = [0]
count_track = 0
count = 0

# Read CSV File
readfile = open('ADC_CSV.csv', 'r')

# Go through each record in the CSV file 
for record in readfile:
    columns = record.split(',')
    count += 1
    
    if count % 500 == 0:
        count_track += 1
        mf2_anem_dir.append(columns[1])
        mf2_anem_spd.append(columns[3])
        ship_anem_ws_2_dir.append(columns[4])
        ship_anem_ws_2_spd.append(columns[5])
        ship_anem_ws_3_dir.append(columns[6])
        ship_anem_ws_3_spd.append(columns[7])
        x_axis.append(count_track)
        
fig1 = pl.figure(1)

# Plot Windspeed and Direction
pl.subplot(311)
plot1 = pl.plot(mf2_anem_dir, mf2_anem_spd, 'ro')
pl.title('MF2(RED) Fwd Port (GRE) Aft Stbd (BLU)')
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)

pl.subplot(312)
plot2 = pl.plot(ship_anem_ws_2_dir, ship_anem_ws_2_spd, 'go')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)

pl.subplot(313)
plot3 = pl.plot(ship_anem_ws_3_dir, ship_anem_ws_3_spd, 'bo')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)

"""
fig2 = pl.figure(2)
pl.subplot(311)
plot4 = pl.plot(x_axis, mf2_anem_spd, 'ro')
pl.title('MF2(RED) SHIP 1 (GRE) SHIP 2 (BLU)')
pl.ylabel('Wind Speed')
pl.subplot(312)
plot5 = pl.plot(x_axis, ship_anem_ws_2_spd, 'go')
pl.subplot(313)
plot6 = pl.plot(x_axis, ship_anem_ws_3_spd, 'bo')
"""

pl.show()

readfile.close()

input("Press any key to continue. ")