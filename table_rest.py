import numpy as np
white_table = np.array([[0 for i in range(8)]for i in range(8)])
black_table = np.array([[0 for i in range(8)]for i in range(8)])
np.save("white_table.npy", white_table)
np.save("black_table.npy", black_table)
