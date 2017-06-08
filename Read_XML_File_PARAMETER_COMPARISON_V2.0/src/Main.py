# Read XML File
# Parse XML file and get roots (elements)
import xml.etree.ElementTree as ET
tree = ET.parse('TrialSummaryFile.xml')
root = tree.getroot()

# Take input from the user:
# 1. Parameter of interest - child of 'Evolution' tag
# 2. Threshold data is the limit of interest - this only assesses the value itself
set_param = input("Enter parameter of interest: ")
set_threshold = input("Enter threshold data: ")

# Determine the number of Evolutions in this segment
count_evol = 0
for XML_PARSE in root.findall("./Evolutions/Evolution"):
    count_evol = count_evol + 1

# Commence the search loop - iterate through Evolution Numbers for Desired Parameter
for x in range(1, count_evol + 1):
    evol_id = "'%s'" % x
    thresh_val = "'%s'" % set_threshold
    check_param = "./Evolutions/Evolution/[ID=%s]/*[%s=%s]" % (evol_id, set_param, thresh_val)

# Within loop - if parameter is found that meets the threshold value, then set flag
    flag = 0
    for XML_PARSE in root.findall(check_param):
        flag = 1
# If flagged, then print ID value that has met the threshold
    if flag == 1:
        print("Evolution Number: %s has %s threshold value of %s" % (evol_id, set_param, thresh_val))
    else:
        continue
input("Press any key to exit.")
