import pandas as pd

#Input the file name here (without the ".txt") note that for the program to work, the ascii file 
#must be downloaded to the repository 
fileName = ""

#Opens up the file from the repository and creates a list seperated by return statements in the txt file
infile = open(f"{fileName}.txt", "r", encoding = "IOS 8859-1")
lines = infile.readlines()

#Seperates the information provided by the unfiltered EIS data file into the inputs before the
#experiment starts, headers, and the raw data obtained from the EIS sample run
EIS_runInformaton = lines[:3]
headers = lines[3].strip().split(",")
data = lines[4:]

#Takes the experimental data and converts it into a list that can be put into a table (DataFrame)
dataRows = [line.strip().split(",") for line in data[:]]
df = pd.DataFrame(dataRows, columns = headers)
outfile = f"{fileName}.xlsx"

#Converts the DataFrame into an excel document that can be downladed off of the repository
df.to_excel(sheet_name = fileName, index = False, excel_writer = outfile)
infile.close()
