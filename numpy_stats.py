import numpy as np

marks = np.array([65, 81, 78, 79])
credit_units = np.array([4, 4, 6, 6])

average_mark = np.sum(marks*credit_units) / np.sum(credit_units)
print(f"The average mark of the student is", average_mark) 