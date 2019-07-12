'''import csv

with open('raw_data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close() '''

from matplotlib import pyplot as plt
plt.plot(['a','b','c',],[4,5,1])
plt.show()
