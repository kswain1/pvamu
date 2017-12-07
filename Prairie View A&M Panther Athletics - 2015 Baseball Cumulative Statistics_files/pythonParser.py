import pandas as pd
file = open('SouthernNoClean', 'rw')
cleanFile = open("SouthernClean", 'w')

data = file.read()
data = str(data)
no_commas = data.strip(",")

cleanFile.write(no_commas)
file.close()
cleanFile.close()


southernData = pd.read_csv('SouthernNoClean', delim_whitespace=True)
southernFile = open('SouthernFile.csv', 'w')
print southernData.head()
stringify = str(southernData)
southernFile.write(stringify)
