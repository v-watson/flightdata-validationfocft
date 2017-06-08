# Read CSV File and Analyse Required Params
# Future concept is menu with options for 1. Average 2. Maximum etc.

# Read the csv file into list
readfile = open('evol.csv', 'r')

# Enter parameter of interest
param = input("Enter parameter required as per CSV file: ")
# Create param string for later use
param_string = "%s" % param

# Only Average has been implemented
user_sel = input("Select operation: 1. Average 2. Maximum 3. Minimum: ")
selection = int(user_sel)
if selection == 1:
    print("Average Selected. Calculating...")
    iter_val = 0
    cum_val = 0
    for record in readfile:
        columns = record.split(',')
        value = 0
        if columns[1].count(param_string) == 1:
            value = float(columns[2])
            iter_val = iter_val + 1
            cum_val = value + cum_val
            average = cum_val/iter_val
        else:
            continue
    print(average)
elif selection == 2:
    print("Maximum Selected. Calculating...")
elif selection == 3:
    print("Minimum Selected. Calculating...")

input("Press any key to continue.")
