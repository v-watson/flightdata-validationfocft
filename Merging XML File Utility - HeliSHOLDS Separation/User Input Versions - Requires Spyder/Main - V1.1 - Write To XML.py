# Utility to ease the merging of XML files for Trial Summary File separation with HeliSHOLDS
# VERSION 1.1 - Write to XML 

import linecache

readfile = open('TrialSummaryFile.xml', 'r')
writefile = open('TrialSummaryFile_Updated.xml', 'w')

line_count = 0
end_sorties = 0
end_evolutions = 0
bool_check = 0
size_of_evolutions = 0
size_of_sorties = 0
size_of_tsv = 0

# Determine where </Sorties> tag is in TSV
for line in readfile:
    bool_check = line.find('</Sorties>')
    
    if bool_check > 0:
        end_sorties = line_count
        line_count += 1
    else:
        line_count += 1    
        
print("</Sortie> tag in Sorties File is %s" % str(end_sorties))

# Reset procedure - line count, bool check and re-open file
line_count = 0
readfile = open('TrialSummaryFile.xml', 'r')
bool_check = 0

# Determine where </Evolutions> tag is in TSV
for line in readfile:
    bool_check = line.find('</Evolutions>')
    
    if bool_check > 0:
        end_evolutions = line_count
        line_count += 1
    else:
        line_count += 1  
        
print("</Evolutions> tag in Evolutions File is %s" % str(end_evolutions))

# Reset procedure - line count and re-open file
line_count = 0
readfile = open('Evolutions.xml', 'r')

# Determine size of evolutions file
for line in readfile:
    line_count += 1
    
size_of_evolutions = line_count        
print("Evolutions File size is %s" % str(size_of_evolutions))

# Reset procedure - line count and re-open file
line_count = 0
readfile = open('Sorties.xml', 'r')

# Determine size of sorties file
for line in readfile:
    line_count += 1  

size_of_sorties = line_count        
print("Sorties File size is %s" % str(size_of_sorties))

# Reset procedure - line count and re-open file
line_count = 0
readfile = open('TrialSummaryFile.xml', 'r')

# Determine size of TSV
for line in readfile:
    line_count += 1  

size_of_tsv = line_count        
print("TS File size is %s" % str(size_of_tsv))

# Commence re-writing TSV file with new sortie and evolution information
total_size_tsvu = size_of_tsv + size_of_sorties + size_of_evolutions
line_write = 0
print("New TSF size is %s" % str(total_size_tsvu))

# Logic in this section to add new sortie and evolution sections
while (line_write <= total_size_tsvu):
    line_write_sort = 0
    line_write_evol = 0
    
    if line_write == end_sorties:
        write_line = linecache.getline('TrialSummaryFile.xml', line_write)
        writefile.write(write_line)
        while(line_write_sort <= size_of_sorties):
            write_sort_line = linecache.getline('Sorties.xml', line_write_sort)
            writefile.write(write_sort_line)
            line_write_sort += 1
    elif line_write == end_evolutions:
        write_line = linecache.getline('TrialSummaryFile.xml', line_write)
        writefile.write(write_line)
        while(line_write_evol <= size_of_evolutions):
            write_evol_line = linecache.getline('Evolutions.xml', line_write_evol)
            writefile.write(write_evol_line)
            line_write_evol += 1
    else:
        write_line = linecache.getline('TrialSummaryFile.xml', line_write)
        writefile.write(write_line)
        
    line_write += 1

print("Generated TSF_Updated size is %s" % str(line_write))
   
writefile.close() 
readfile.close()