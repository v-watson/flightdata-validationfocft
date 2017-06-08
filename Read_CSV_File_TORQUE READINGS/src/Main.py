# Read CSV File

readfile = open('evol.csv', 'r')

# list_storage = readfile.readlines()
# list_storage = ["one", "two", "three"]
# list_size = len(list_storage)
# print(list_size)
# list_storage.index('2016-08-09T11:05:31.5645182+10:00,EGI1_RT03_SA03_TX_W03,10982,System.UInt16')
# print(list_storage.index("one"))
# print(list_storage[2])
# list_storage.sort()
# print(list_storage[0])

for record in readfile:
    columns = record.split(',')
    value = 0
    if columns[1].count('TORQUE') == 1:
        value = float(columns[2])
        if value > 60:
            print('EXCEEDANCE')
        else:
            continue
    else:
        continue
