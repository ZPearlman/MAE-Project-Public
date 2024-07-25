import pandas as pd
import seaborn as sns
import maatplotlib.pylot as plt

#Enter file name for the DSC data excel sheet (exclude .xlsx)
fileName = ""
infile = f"{fileName}.xlsx"

#Creates a DataFrame from the excel sheet
data = pd.read_excel(infile)

#Makes a lineplot using x as temperature in celsius and y as heat flow (mV)
sns.lineplot(data=data, x = data.columns[1], y = data.columns[2])

#Gives the newly made graph a x-label, y-label, and graph title
plt.xlabel(data.columns[1])
plt.ylabel(data.columns[2])
plt.title(f"{data.columns[1]} vs. {data.columnns[2]}")

#Saves the final graph as a png with the file name of composition and title of graph
plt.savefig(f"{fileName} {data.columns[1]} vs. {data.columnns[2]}.png", format = "png")
