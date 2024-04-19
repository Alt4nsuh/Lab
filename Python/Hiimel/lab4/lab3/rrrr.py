import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def switch(x):
    if x == (0,0):
        return 1
    elif x == (0,1):
        return 2
    elif x == (0,2):
        return 3
    elif x == (1,0):
        return 4
    elif x == (1,1):
        return 5
    elif x == (1,2):
        return 6
    elif x == (2,0):
        return 7
    elif x == (2,1):
        return 8
    elif x == (2,2):
        return 9
 
def shuffle_and_reconstruct(input_image_path):
    image = mpimg.imread(input_image_path)
    height, width, _ = image.shape

    sub_width = width // 3
    sub_height = height // 3

    sub_images = []
    indices = []  # Keep track of original indices

    for i in range(3):
        for j in range(3):
            left = j * sub_width
            upper = i * sub_height
            right = (j + 1) * sub_width
            lower = (i + 1) * sub_height

            sub_image = image[upper:lower, left:right, :]
            sub_images.append(sub_image)
            indices.append((i, j))  # Save the original indices

    shuffled_indices = list(range(9))
    random.shuffle(shuffled_indices)  # Shuffle the list of indices
    ind = indices.copy()
    new_image = np.zeros_like(image)

    for i, shuffled_index in enumerate(shuffled_indices):
        original_index = indices[shuffled_index]
        row, col = original_index
        left = col * sub_width
        upper = row * sub_height
        print(row,col," ",original_index)

        new_image[upper:upper + sub_height, left:left + sub_width, :] = sub_images[i]
        ind[i] = switch(original_index)
    b=ind.copy()
    for i,ii in enumerate(ind):
        b[ii-1]=i+1
    ind_array = np.array(b)
    ind_array = ind_array-1
    a= ind_array.reshape(3,3)
    return a,new_image



def reconstruct(x,input_image_path):
    image = input_image_path
    # height, width, _ =x

    # sub_width = width // 3
    # sub_height = height // 3

    # sub_images = []
    # indices = []  # Keep track of original indices

    # for i in range(3):
    #     for j in range(3):
    #         left = j * sub_width
    #         upper = i * sub_height
    #         right = (j + 1) * sub_width
    #         lower = (i + 1) * sub_height

    #         sub_image = image[upper:lower, left:right, :]
    #         sub_images.append(sub_image)
    #         indices.append((i, j))  
    plt.imshow(input_image_path)  
    plt.show()


