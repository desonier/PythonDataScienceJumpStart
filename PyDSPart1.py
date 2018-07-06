
import random 
rand_ages=[random.randrange(1,100,1,int) for _ in range (100)]
#print(rand_ages)

import numpy as np
np_x = np.array(rand_ages) 
print(np_x)

import matplotlib as mpl

mpl.plot(np_x)
mpl.show()
