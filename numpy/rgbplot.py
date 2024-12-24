#storing rgb data in a 3d array.

import numpy as np

rgb_example = np.array([[[255, 0, 0], [255, 255, 0], [255, 255, 255]],
               			[[255, 0, 255], [0, 255, 0], [0, 255, 255]],
               			[[0, 0, 0], [0, 255, 255], [0, 0, 255]]])
#in the tuple, we're passing first a list of each row, 
#then a list of the pixels in that row
#then the rgb values of the pixel itself in the row.
#let's visualize it with matplotlib (to be covered later)

import matplotlib.pyplot as plt
plt.imshow(rgb_example)
plt.show()