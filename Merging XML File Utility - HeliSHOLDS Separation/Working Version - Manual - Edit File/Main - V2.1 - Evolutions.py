# Utility to ease the merging of XML files for Trial Summary File separation with HeliSHOLDS
# VERSION 2.1 

import linecache
import re

readfile = open('TrialSummaryFile.xml', 'r')
writefile = open('Evolutions.xml', 'w')

line_count = 0

for line in readfile:
    matchObj = re.search( r'2016-08-10', line, re.X|re.I)
    line_count += 1
    
    if matchObj:
        ev_start = line_count - 1
        ev_search = linecache.getline('TrialSummaryFile.xml', ev_start)
               
        bool_search = ev_search.find('<Evolution>')
        
        x = 0
        if bool_search > 0:
            while (x < 2000):
                evol_line = linecache.getline('TrialSummaryFile.xml', ev_start + x)
                bool_term_string = evol_line.find('</Evolution>')
                writefile.write(evol_line)
                if bool_term_string > 0:
                    x = 2000
                else:
                    x += 1
        else:
            continue
        
    else:
        continue
   
writefile.close() 
readfile.close()
    
#input("Press any key to continue.")
