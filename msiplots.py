#install required libraries
#pip3 install matplotlib
#pip3 install Tkinter
import matplotlib
from matplotlib import pyplot as plt
import tkinter as tk
import tkinter.filedialog 
from tkinter.filedialog import askopenfilename


filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
print("where do you want to save your graphs?")
directory = tkinter.filedialog.askdirectory()

fig = plt.figure(figsize=(50, 30))
fig.subplots_adjust(hspace = 1, wspace = 1)
position = 1

with open(filename) as f:
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
            print("plotting read count distribution")
            if total>20: #only selects those sites where coverage >20 as these are the only ones used to generated the MSI score
                ax = plt.subplot(10,10,position)
                ax.plot(data) # plots list of numbers (ie read count distribution) as a line graph
                plt.xlabel("Repeat length")
                plt.ylabel("Frequency")
                plt.title(graph_title)
                position= position + 1

plt.savefig(directory+"/"+"graph.png")
print("file saved to", directory)


                

