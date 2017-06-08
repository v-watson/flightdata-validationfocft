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
ship_anem_ws_1_dir = [0]
ship_anem_ws_1_spd = [0]
ship_anem_ws_2_dir = [0]
ship_anem_ws_2_spd = [0]
ship_anem_ws_3_dir = [0]
ship_anem_ws_3_spd = [0]
mf2_shipanem_diff_ws1 = [0]
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
        mf2_anem_spd.append(columns[2])
        ship_anem_ws_1_dir.append(columns[3])
        ship_anem_ws_1_spd.append(columns[4])
        ship_anem_ws_2_dir.append(columns[5])
        ship_anem_ws_2_spd.append(columns[6])
        ship_anem_ws_3_dir.append(columns[7])
        ship_anem_ws_3_spd.append(columns[8])
        
        mf2_shipanem_diff_ws1.append(float(columns[4]) - float(columns[2]))
        mf2_shipanem_diff_ws2.append(float(columns[6]) - float(columns[2]))
        mf2_shipanem_diff_ws3.append(float(columns[8]) - float(columns[2]))
        
fig1 = pl.figure(1)

# Plot Windspeed and Direction
pl.subplot(411)
plot1 = pl.plot(mf2_anem_dir, mf2_anem_spd, 'ro')
pl.title('MF2(RED) Fwd Stbd (YEL) Fwd Port (GRE) Aft Stbd (BLU)')
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

pl.subplot(412)
plot2 = pl.plot(ship_anem_ws_1_dir, ship_anem_ws_1_spd, 'yo')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

pl.subplot(413)
plot3 = pl.plot(ship_anem_ws_2_dir, ship_anem_ws_2_spd, 'go')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

pl.subplot(414)
plot4 = pl.plot(ship_anem_ws_3_dir, ship_anem_ws_3_spd, 'bo')
pl.ylim(0, 20)
pl.xlabel('Wind Direction Relative')
pl.ylabel('Wind Speed')
pl.xlim(-200, 200)
pl.grid(True)

fig2 = pl.figure(2)
pl.subplot(311)
plot1 = pl.plot(mf2_anem_dir, mf2_shipanem_diff_ws2, 'ro')
pl.title('MF2 to FWD Port Difference (RED)')
pl.xlabel('Wind Direction Relative (deg)')
pl.ylabel('Wind Speed Difference (kts)')
#pl.xlim(-200, 200)
pl.ylim(-30, 30)
pl.grid(True)

pl.subplot(312)
plot2 = pl.plot(mf2_anem_dir, mf2_shipanem_diff_ws3, 'go')
pl.title('MF2 to AFT Stbd Difference (GREEN)')
pl.xlabel('Wind Direction Relative (deg)')
pl.ylabel('Wind Speed Difference (kts)')
#pl.xlim(-200, 200)
pl.ylim(-30, 30)
pl.grid(True)

pl.subplot(313)
plot3 = pl.plot(mf2_anem_dir, mf2_shipanem_diff_ws1, 'bo')
pl.title('MF2 to FWD Stbd Difference (BLUE)')
pl.xlabel('Wind Direction Relative (deg)')
pl.ylabel('Wind Speed Difference (kts)')
#pl.xlim(-200, 200)
pl.ylim(-30, 30)
pl.grid(True)

pl.show()

readfile.close()

input("Press any key to continue. ")