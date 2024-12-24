#Image rgb information can be stored in a NumPy array and saved as a .npy file.
#in the assets folder, we've got one called: dc_logo_rgb_array.npy.

#We can load the array using np.load():

import numpy as np

black_logo = np.load("assets/dc_logo_rgb_array.npy") #throws error if inline terminal isn't navigated to my working directory, just do that.
print(black_logo) #see the data in it

import matplotlib.pyplot as plt

plt.imshow(black_logo)
plt.show()

#now, using the np.where() function, we can replace all 0 values (black) with 255 (white).
white_logo = np.where(black_logo==0, 255, black_logo)
#white_logo = np.where(black_logo==[0, 0, 0], [255, 255, 255], black_logo) also works

plt.imshow(white_logo)
plt.show()

#we can replace the green part with pink (pixel value: r=255, g=110, b=169)
pink_logo = np.where(black_logo!=[0, 0, 0], [255, 110, 169], black_logo) #replace the pixels not black [0, 0, 0], with the pink pixel [255, 110, 169]

plt.imshow(pink_logo)
plt.show()