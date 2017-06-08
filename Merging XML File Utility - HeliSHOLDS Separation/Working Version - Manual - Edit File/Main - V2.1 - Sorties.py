# Utility to ease the merging of XML files for Trial Summary File separation with HeliSHOLDS
# VERSION 1.1 - Sorties - Reads TrialSummaryFile and copies Sortie Data for date of interest

import linecache
import re

readfile = open('TrialSummaryFile.xml', 'r')
writefile = open('Sorties.xml', 'w')

line_count = 0

for line in readfile:
    matchObj = re.search(r'2016-08-09', line, re.X|re.I)
    line_count += 1
    
    if matchObj:
        sortie_start = line_count - 4
        search_sortie = linecache.getline('TrialSummaryFile.xml', sortie_start)
        
        bool_search = search_sortie.find('<Sortie>')
        
        x = 0
        if bool_search > 0:
            while (x < 300):
                sortie_line = linecache.getline('TrialSummaryFile.xml', sortie_start + x)
                bool_term_string = sortie_line.find('</Sortie>')
                writefile.write(sortie_line)
                if bool_term_string > 0:
                    x = 300
                else:
                    x += 1
        else:
            continue
    else:
        continue
   
writefile.close() 
readfile.close()
    
#input("Press any key to continue.")
