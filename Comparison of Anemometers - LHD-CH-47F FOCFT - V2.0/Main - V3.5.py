"""
Title: Anemometer Comparison Script
Date: 23 Aug 16
Author: Viruben
"""

import pylab as pl

# CSV sorted initially using Excel
# FWD Port -Ship's An 2
# AFT Stbd - Ship's An 3

# Set variables for plot
mf2_anem_dir = [0]
mf2_anem_spd = [0]
ship_anem_ws_2_dir = [0]
ship_anem_ws_2_spd = [0]
ship_anem_ws_3_dir = [0]
ship_anem_ws_3_spd = [0]
mf2_shipanem_diff_ws2 = [0]
mf2_shipanem_diff_ws3 = [0]
count = 0

# Read CSV File
readfile = open('ADC_CSV.csv', 'r')

# Go through each record in the CSV file 
for record in readfile:
    columns = record.split(',')
    count += 1
    
    if count % 10 == 0:
        mf2_anem_dir.append(columns[1])
        mf2_anem_spd.append(columns[3])
        ship_anem_ws_2_dir.append(columns[4])
        ship_anem_ws_2_spd.append(columns[5])
        ship_anem_ws_3_dir.append(columns[6])
        ship_anem_ws_3_spd.append(columns[7])
        
        mf2_shipanem_diff_ws2.append(float(columns[5]) - float(columns[3]))
        mf2_shipanem_diff_ws3.append(float(columns[7]) - float(columns[3]))
        
fig1 = pl.figure(1)

# Plot Windspeed and Direction
pl.subplot(311)
plot1 = pl.plot(mf2_anem_dir, mf2_anem_spd, 'ro')
pl.title('MF2(RED) Fwd Port (GRE) Aft Stbd (BLU)')
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

pl.subplot(312)
plot2 = pl.plot(ship_anem_ws_2_dir, ship_anem_ws_2_spd, 'go')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

pl.subplot(313)
plot3 = pl.plot(ship_anem_ws_3_dir, ship_anem_ws_3_spd, 'bo')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

fig2 = pl.figure(2)
pl.subplot(211)
plot1 = pl.plot(mf2_anem_dir, mf2_shipanem_diff_ws2, 'ro')
pl.title('MF2 to FWD Port Difference (RED)')
pl.xlabel('Wind Direction Relative (deg)')
pl.ylabel('Wind Speed Difference (kts)')
#pl.xlim(-200, 200)
pl.ylim(-30, 30)
pl.grid(True)

pl.subplot(212)
plot2 = pl.plot(mf2_anem_dir, mf2_shipanem_diff_ws3, 'go')
pl.title('MF2 to AFT Stbd Difference (GREEN)')
pl.xlabel('Wind Direction Relative (deg)')
pl.ylabel('Wind Speed Difference (kts)')
#pl.xlim(-200, 200)
pl.ylim(-30, 30)
pl.grid(True)

pl.show()

readfile.close()

input("Press any key to continue. ")