# NumPy: Apply a Mask from one Array to another Array

import numpy as np

x = np.array([1, 3, 5, 7, 9, 12])
y = np.array([2, 4, 6, 8, 10, 14])

masked_y_array = np.ma.masked_where(y > 8, y)

# filter out values in `y` that are greater than 8
print(masked_y_array)  # 👉️ [2 4 6 8 -- --]

new_x_array = np.ma.masked_where(np.ma.getmask(masked_y_array), x)

# apply the mask of `masked_y_array` to `x`
print(new_x_array)  # 👉️ [1 3 5 7 -- --]