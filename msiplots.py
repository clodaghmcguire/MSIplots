#install required libraries
#pip3 install matplotlib

import matplotlib
from matplotlib import pyplot as plt

with open(63f8c42f.tumor.prefix_dis) as f: #opens output file from msisensor2
    read_data = f.readlines() # reads each line in file
    #print(read_data)
    for line in read_data:
        #print(line)
        c = line.startswith("chr")
        if c is True:
            graph_title = line.strip()
        s = line.startswith("T:") # looks for lines that start with T: as these are the lines with read count distribution
        #print(s)
        if s is True:
            #print(line)
            #remove T: from start of line and turn line into list of strings
            data = line.strip("T:")
            data = data.split()
            data = [int(i) for i in data] # turn list of strings into list of integers
            total = sum(data)
            print("plotting read count distribution")
            if total>0: 
                plt.plot(data) # plots list of numbers (ie read count distribution) as a line graph
                plt.xlabel("Repeat length")
                plt.ylabel("Frequency")
                plt.show()
                