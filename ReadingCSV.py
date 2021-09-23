# Read CSV File
import numpy as np
reading_csv = np.loadtxt("main.csv", delimiter=",")
var = reading_csv[:4, :]
print(var)
