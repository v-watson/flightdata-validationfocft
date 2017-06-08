# This file reads in azimuth and spot number for the purposes of torque and DIPES comparison
# V. Watson - 17 AUG 16 - V2.0
# NOTE: Requires DIPES displayed to be highest - currently only one rating displayed

# Read XML File
# Parse XML file and get roots (elements)
import xml.etree.ElementTree as ET
tree = ET.parse('TrialSummaryFile.xml')
root = tree.getroot()

# Take in and store user input
print("The following will compare spots based on azimuth and speed (within +/-10 deg and +/-5kts)")
set_sector = input("Enter 'R' or 'G' for Red or Green wind: ")
set_azimuth = int(input("Enter Degrees: "))
set_spd = input("Enter Speed (min 20): ")
set_spot = input("Enter Spot Number: ")

# Setting user variables for later use
abs_azi = 0
abs_spd = 0
abs_spd = int(set_spd)
spot_no = "'%s'" % set_spot

# Convert input from red and green reference to 360 deg reference
if set_sector == "r" or set_sector == "R":
    abs_azi = 360 - set_azimuth
    print("Azimuth required: %s" % abs_azi)
elif set_sector == "g" or set_sector == "G":
    abs_azi = set_azimuth
    print("Azimuth required: %s" % abs_azi)
else:
    print("Cannot understand selection. Please select either 'R' or 'G'")

# Commence printing output
print("The following EV IDs meet the wind conditions at Spot %s:" % spot_no)
print("Value of ZERO indicates no data available.")
# Determine the number of Evolutions in this segment
count_evol = 0
for XML_PARSE in root.findall("./Evolutions/Evolution"):
    count_evol = count_evol + 1

# Commence the search loop - this will find specific variables for each spot (inc. torque, wind etc.)
for x in range(1, count_evol + 1):
    evol_id = "'%s'" % x
    check_spot = "./Evolutions/Evolution/[ID=%s]/[Spot=%s]" % (evol_id, spot_no)
    check_dir = "./Evolutions/Evolution/[ID=%s]/RelativeWindReference/Direction" % (evol_id)
    check_spd = "./Evolutions/Evolution/[ID=%s]/RelativeWindReference/Speed" % (evol_id)
    check_torque = "./Evolutions/Evolution/[ID=%s]/TorqueSteadyStateAbsMarginPercent" % (evol_id)
    check_PSA = "./Evolutions/Evolution/[ID=%s]/PRS/PreditabilityAndSituationalAwareness" % (evol_id)
    check_accuracy = "./Evolutions/Evolution/[ID=%s]/PRS/Accuracy" % (evol_id)  # Need to USE this
    check_limits = "./Evolutions/Evolution/[ID=%s]/PRS/Limits" % (evol_id)  # Need to USE this

    # Commence loops which conduct iterative search for each parameter - once one level found then
    # proceed to next level i.e. start at checking spot, move down to wind direction, once confirmed
    # wind is within requested azimuth, proceed to wind speed and continue till all values consequently
    # printed for the requested condition
    for XML_PARSE in root.findall(check_spot):
        for XML_PARSE in root.findall(check_dir):
            dir_val = float(XML_PARSE.text)
            # logic to determine whether this wind direction falls in scope
            if (dir_val <= abs_azi + 5 and dir_val >= abs_azi - 5) or dir_val <= (abs_azi + 5) - 360 or dir_val >= (
                abs_azi - 5) + 360:
                for XML_PARSE in root.findall(check_spd):
                    spd_val = float(XML_PARSE.text)
                    PSA_val = 0
                    acc_val = 0
                    lim_val = 0
                    tq_val = 0
                    # logic to determine whether wind speed falls in scope
                    if spd_val <= abs_spd + 20 and spd_val >= abs_spd - 20:
                        for XML_PARSE in root.findall(check_PSA):
                            PSA_val = float(XML_PARSE.text)
                        for XML_PARSE in root.findall(check_accuracy):
                            acc_val = float(XML_PARSE.text)
                        for XML_PARSE in root.findall(check_limits):
                            lim_val = float(XML_PARSE.text)
                        for XML_PARSE in root.findall(check_torque):
                            tq_val = float(XML_PARSE.text)
                        
                        # Confirm max DIPES rating
                        dipes_val = max(PSA_val, acc_val, lim_val)
                       # print("EV ID %s has Wind Speed %s kts" % (evol_id, spd_val))
                       # print("EV ID %s has Wind Direction %s deg" % (evol_id, dir_val))
                        print("EV ID %s has DIPES %s" % (evol_id, dipes_val))
                        print("EV ID %s has TQ margin of %s pct" % (evol_id, tq_val))

                    else:
                        continue

            else:
                continue

input("Press any key to exit.")
