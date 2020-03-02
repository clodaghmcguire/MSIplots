"""
This program takes the read count distribution output file from msisensor2 (output.prefix_dis) 
and plots the distribution for all microsatellite and homopolymer sites that meet the required
coverage. The chosed coverage should match what was entered into msisensor2 (default is 20)

msisensor2 is available at https://github.com/niu-lab/msisensor2
"""


#install required libraries
#pip3 install matplotlib
#pip3 install Tkinter
import matplotlib
from matplotlib import pyplot as plt
import tkinter as tk
import tkinter.filedialog 
from tkinter.filedialog import askopenfilename
import os
import numpy as np

filelocation = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filelocation)
filename = os.path.split(filelocation)[1]
print("where do you want to save your graphs?")
directory = tkinter.filedialog.askdirectory()
print(directory)
coverage = int(input("what coverage?"))

fig = plt.figure(figsize=(50, 30))
fig.subplots_adjust(hspace = 1, wspace = 1)
position = 1

with open(filelocation) as f:
    read_data = f.readlines() # reads each line in file
    for line in read_data:
        c = line.startswith("chr")
        if c is True:
            graph_title = line.strip()
        s = line.startswith("T:") # looks for lines that start with T: as these are the lines with read count distribution
        if s is True:
            #remove T: from start of line and turn line into list of strings
            data = line.strip("T:")
            data = data.split()
            data = [int(i) for i in data] # turn list of strings into list of integers
            total = sum(data)
            
            if total>coverage: #only selects those sites where coverage is high enough be to used to generate MSI score
                print("plotting read count distribution")
                ax = plt.subplot(8,4,position)
                ax.bar(np.arange(len(data)), data) # plots list of numbers (ie read count distribution) as a bar graph
                plt.xlim(right=40) #limits x-axis to 40 so that you can see spread of distribution clearly
                plt.xlabel("Repeat length")
                plt.ylabel("Frequency")
                plt.title(graph_title)
                position= position + 1

plt.savefig(directory+"/"+filename+".png")
print("file saved to", directory)


                

