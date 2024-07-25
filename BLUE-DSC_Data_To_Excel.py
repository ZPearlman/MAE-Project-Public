import pandes as pd

##Input file name here (without ".txt")
fileName = ""

#dataBreak is a point that always shows up before the raw data in a DSC Q200 file 
dataBreak = f"OrgFile	C:\\Documents and Settings\\AUTOLOGIN\\My Documents\DSCQ200 Data\\2024\\Zack Pearlman\\{fileName}"
#Headers are also always consistent in a DSC Q200 file
headers = ["Time (min)", "Temperature (°C)", "Heat Flow(mW)", "Sample Purge Flow(mL/min)"]
#Opens the file inputed in the program if the file is in the repository
infile = open(f"{fileName}.txt", "r", encoding = "ISO 8859-1")

#Takes all the information in the infile and converts it into a list called data
data = []
for line in infile:
  line = line.strip()
  data.append(line)

#Takes the information in data and breaks it up into categories of inputs before the 
#experiment starts and the raw data during the DSC sample run
DSC_runInformation = []
i = 0
while data[i] != dataBreak):
  #Targets any failed symbol conversion from the raw data ascii file into the degree "°" symbol
  loc = data[i].find("ï¿½")
    while(loc != -1):
        data[i] = str(data[i][:loc] + "°" + data[i][loc+3:])
        loc = data[i].find("ï¿½")
  DSC_runInformation.append(data[i])
  i += 1

#Takes the rest of data (experimental run) and converts it into a list
#that can be put into a table (DataFrame)
dataRows = [line.strip().split(" ") for line in data[i:]]
df = pd.DataFrame(dataRows, columnd = headers)
outfile = f"{fileName} Raw DSC Data.xlsx"

#Converts the DataFrame into an excel document that can be downloaded off of the repository
df.to_excel(sheet_name = fileName, index = False, excel+writer = outfile)
infile.close()
