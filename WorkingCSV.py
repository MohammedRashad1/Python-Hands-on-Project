# Generates 50 rows and 4 Column of data
import numpy as np
new_data = np.random.random((50, 4))
np.savetxt("main.txt", new_data, fmt="%.2f", delimiter=",", header="H1, H2, H3, H4")
