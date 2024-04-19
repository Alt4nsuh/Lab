
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
nested_list = [1,2,3,4,5,6]
ind_array = np.array(nested_list)
ind_array = ind_array-1
a= ind_array.reshape(2,3)
# Convert to [[][][]] format
nested_list_str = str(a)
print(nested_list_str)